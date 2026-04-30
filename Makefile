.DEFAULT_GOAL := help

VENV   := .venv
PYTHON := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip

.PHONY: help venv install lint format test

help: ## Show available make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

venv: ## Create .venv virtual environment
	python3 -m venv $(VENV)

install: venv ## Install dev dependencies into .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-dev.txt

lint: ## Run ruff linter
	$(PYTHON) -m ruff check .

format: ## Run ruff formatter
	$(PYTHON) -m ruff format .

test: ## Run pytest
	$(PYTHON) -m pytest
