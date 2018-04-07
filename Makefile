init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	pipenv run pytest

lint:
	pipenv run flake8 --ignore F401 pwnedapi

coverage:
	pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov-report html --cov=pwnedapi pwnedapi
