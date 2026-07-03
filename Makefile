SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -euo pipefail -c

CONFIG_FILE := input/config.json

.PHONY: all build run-analysis publish generate_landing_page

all: build run-analysis publish generate_landing_page

build:
	@echo "Starting build..."
	if command -v uv >/dev/null 2>&1 && [ -d ".venv" ]; then \
		echo "Using uv environment (.venv detected)."; \
		uv sync; \
	else \
		echo "Using pip fallback (uv missing or .venv not found)."; \
		if [ -x ".venv/bin/python" ]; then PYTHON_BIN=".venv/bin/python"; \
		elif command -v python3 >/dev/null 2>&1; then PYTHON_BIN="python3"; \
		elif command -v python >/dev/null 2>&1; then PYTHON_BIN="python"; \
		else echo "Error: No Python interpreter found."; exit 1; fi; \
		"$$PYTHON_BIN" -m pip install --upgrade pip; \
		"$$PYTHON_BIN" -m pip install -e; \
	fi

run-analysis:
	@echo "Running analysis..."
	if command -v uv >/dev/null 2>&1 && [ -d ".venv" ]; then \
		uv run sw-metadata-bot run-analysis --config-file "$(CONFIG_FILE)"; \
	else \
		if [ -x ".venv/bin/python" ]; then PYTHON_BIN=".venv/bin/python"; \
		elif command -v python3 >/dev/null 2>&1; then PYTHON_BIN="python3"; \
		elif command -v python >/dev/null 2>&1; then PYTHON_BIN="python"; \
		else echo "Error: No Python interpreter found."; exit 1; fi; \
		"$$PYTHON_BIN" -m sw_metadata_bot.main run-analysis --config-file "$(CONFIG_FILE)"; \
	fi

publish:
	@echo "Publishing results..."
	if command -v uv >/dev/null 2>&1 && [ -d ".venv" ]; then \
		OUTPUT_DIR=$$(uv run python -c "import read_config; config = read_config.read_config('$(CONFIG_FILE)'); print(read_config.get_output_folder(config))"); \
		LATEST_SUBFOLDER=$$(ls -td "$$OUTPUT_DIR"/*/ | head -1); \
		if [ -z "$$LATEST_SUBFOLDER" ]; then echo "Error: No snapshot folder found under $$OUTPUT_DIR"; exit 1; fi; \
		uv run sw-metadata-bot publish --analysis-root "$$LATEST_SUBFOLDER"; \
	else \
		if [ -x ".venv/bin/python" ]; then PYTHON_BIN=".venv/bin/python"; \
		elif command -v python3 >/dev/null 2>&1; then PYTHON_BIN="python3"; \
		elif command -v python >/dev/null 2>&1; then PYTHON_BIN="python"; \
		else echo "Error: No Python interpreter found."; exit 1; fi; \
		OUTPUT_DIR=$$($$PYTHON_BIN -c "import read_config; config = read_config.read_config('$(CONFIG_FILE)'); print(read_config.get_output_folder(config))"); \
		LATEST_SUBFOLDER=$$(ls -td "$$OUTPUT_DIR"/*/ | head -1); \
		if [ -z "$$LATEST_SUBFOLDER" ]; then echo "Error: No snapshot folder found under $$OUTPUT_DIR"; exit 1; fi; \
		"$$PYTHON_BIN" -m sw_metadata_bot.main publish --analysis-root "$$LATEST_SUBFOLDER"; \
	fi

generate_landing_page:
	@echo "Generating landing page..."
	if command -v uv >/dev/null 2>&1 && [ -d ".venv" ]; then \
		uv run python generate_landing_page.py --config-file "$(CONFIG_FILE)"; \
	else \
		if [ -x ".venv/bin/python" ]; then PYTHON_BIN=".venv/bin/python"; \
		elif command -v python3 >/dev/null 2>&1; then PYTHON_BIN="python3"; \
		elif command -v python >/dev/null 2>&1; then PYTHON_BIN="python"; \
		else echo "Error: No Python interpreter found."; exit 1; fi; \
		"$$PYTHON_BIN" generate_landing_page.py --config-file "$(CONFIG_FILE)"; \
	fi
