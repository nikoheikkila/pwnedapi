init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=$(PWD) pipenv run py.test tests

lint:
	pipenv run flake8 Password

coverage:
	PYTHONPATH=$(PWD) pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov-report html --cov=pwnedapi tests
