install:
	@poetry install

lint:
	@poetry run flake8 tests