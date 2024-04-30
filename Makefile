target = pdf_layout_client

.PHONY: lint
lint:
	poetry run ruff check ${target}
	poetry run mypy ${target}

.PHONY: format
format:
	poetry run ruff format ${target}
	poetry run ruff check --fix ${target}

