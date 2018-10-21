.PHONY: docs

init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

docs:
	pipenv run mkdocs build

test:
	PYTHONPATH=$(PWD) pipenv run pytest

lint:
	pipenv run mypy --strict pwnedapi
	pipenv run pylama --async

coverage:
	PYTHONPATH=$(PWD) pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov-report html --cov=pwnedapi
	codecov --required

publish:
	pipenv run python setup.py install
	pipenv run python setup.py sdist
	pipenv run python setup.py sdist upload
