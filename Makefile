install:
	poetry install

gendiff:
	poetry run gendiff

test:
	poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

publish:
	poetry publish --dry-run


package-install:
	pipx install dist/*.whl

lint:
	poetry run flake8 gendiff

build:
	poetry build

check: test lint

full_ install: install build check publish package-install

