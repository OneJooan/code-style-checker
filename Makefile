.PHONY: install install-dev test check fix clean help

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  install      Install the package (editable)"
	@echo "  install-dev  Install the package + dev dependencies"
	@echo "  test         Run the test suite"
	@echo "  check        Scan the project for style issues"
	@echo "  fix          Scan and auto-fix style issues"
	@echo "  clean        Remove build artifacts and cache files"

install:
	pip install -e .

install-dev:
	pip install -e .
	pip install -r requirements.txt

test:
	pytest tests/

check:
	style-checker .

fix:
	style-checker . --fix

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
