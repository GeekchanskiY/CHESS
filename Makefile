.PHONY: lint format test run

lint:
	ruff check . --fix

format:
	ruff format .

test:
	pytest -v .

run:
	python main.py