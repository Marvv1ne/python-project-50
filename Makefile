install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

check: test lint

full_ install: install build check publish package-install
