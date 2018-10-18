init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=$(PWD) pipenv run pytest

lint:
	pipenv run flake8 --ignore F401 pwnedapi

coverage:
	PYTHONPATH=$(PWD) pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov-report html --cov=pwnedapi

publish:
	pipenv run python setup.py install
	pipenv run python setup.py sdist
	pipenv run python setup.py sdist upload
