init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=$(PWD)/pwnedapi pipenv run pytest

lint:
	pipenv run flake8 Password

coverage:
	PYTHONPATH=$(PWD)/pwnedapi pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov-report html --cov=pwnedapi
