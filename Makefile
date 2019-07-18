.PHONY: docs

init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

docs:
	pipenv run mkdocs build --strict
	@echo "INFO	-  Run 'python3 -m http.server -d site/' to preview."

test:
	PYTHONPATH=$(PWD) pipenv run pytest --workers $(shell nproc)

lint:
	pipenv run mypy --strict pwnedapi
	pipenv run pylama --async

coverage:
	PYTHONPATH=$(PWD) pipenv run pytest --cov-config .coveragerc \
		--cov-report term --cov-report xml --cov-report html \
		--cov=pwnedapi --workers $(shell nproc)
	codecov --required

publish:
	pipenv run python setup.py install
	pipenv run python setup.py sdist
	pipenv run python setup.py sdist upload
