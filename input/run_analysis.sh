#!/bin/bash

# This script runs the analysis workflow and updates the dashboard.
set -euo pipefail

CONFIG_FILE="input/config.json"

USE_UV=false
if command -v uv >/dev/null 2>&1 && [ -d ".venv" ]; then
	USE_UV=true
fi

if [ "$USE_UV" = true ]; then
	echo "Using uv environment (.venv detected)."
	uv sync
else
	echo "Using pip fallback (uv missing or .venv not found)."

	if [ -x ".venv/bin/python" ]; then
		PYTHON_BIN=".venv/bin/python"
	elif command -v python3 >/dev/null 2>&1; then
		PYTHON_BIN="python3"
	elif command -v python >/dev/null 2>&1; then
		PYTHON_BIN="python"
	else
		echo "Error: No Python interpreter found."
		exit 1
	fi

	"$PYTHON_BIN" -m pip install --upgrade pip
	"$PYTHON_BIN" -m pip install "pystache>=0.6.8" "rsmetacheck>=0.3.1" "sw-metadata-bot>=0.4.3"
fi

if [ "$USE_UV" = true ]; then
	uv run --with sw-metadata-bot sw-metadata-bot run-analysis --config-file "$CONFIG_FILE"
else
	"$PYTHON_BIN" -m sw_metadata_bot.main run-analysis --config-file "$CONFIG_FILE"
fi

echo "Analysis completed. Publishing results to respective repositories..."

if [ "$USE_UV" = true ]; then
	OUTPUT_DIR=$(uv run python -c "import read_config; config = read_config.read_config('$CONFIG_FILE'); print(read_config.get_output_folder(config))")
else
	OUTPUT_DIR=$(
		"$PYTHON_BIN" -c "import read_config; config = read_config.read_config('$CONFIG_FILE'); print(read_config.get_output_folder(config))"
	)
fi

# Get latest snapshot folder from output directory.
LATEST_SUBFOLDER=$(ls -td "$OUTPUT_DIR"/*/ | head -1)
if [ -z "${LATEST_SUBFOLDER:-}" ]; then
	echo "Error: No snapshot folder found under $OUTPUT_DIR"
	exit 1
fi

if [ "$USE_UV" = true ]; then
	uv run --with sw-metadata-bot sw-metadata-bot publish --analysis-root "$LATEST_SUBFOLDER"
else
	"$PYTHON_BIN" -m sw_metadata_bot.main publish --analysis-root "$LATEST_SUBFOLDER"
fi

echo "Issues submitted to the repositories"

if [ "$USE_UV" = true ]; then
	uv run python generate_landing_page.py --config-file "$CONFIG_FILE"
else
	"$PYTHON_BIN" generate_landing_page.py --config-file "$CONFIG_FILE"
fi