.PHONY: lint format test

lint:
	ruff check . --fix

format:
	ruff format .

test:
	pytest -v .
