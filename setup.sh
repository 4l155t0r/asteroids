#!/usr/bin/env bash
set -e

# 1. Create project (skip if already done)
if [ ! -f "pyproject.toml" ]; then
    echo "pyproject.toml not found. Did you already run 'uv init <project-name>'?"
    echo "If not, run that first from the folder *above* this one."
    exit 1
fi

# 2. Pin Python 3.13 (idempotent)
uv python pin 3.13

# 3. Create venv (safe to run multiple times)
if [ ! -d ".venv" ]; then
    uv venv
fi

# 4. Activate venv
#   (this assumes macOS/Linux layout like in the lesson)
# shellcheck disable=SC1091
# source .venv/bin/activate
# Activate manually

# 5. Add pygame dependency (safe to re-run with same version)
uv add pygame==2.6.1

echo
echo "Setup complete."
echo "To use this project later, activate the venv with:"
echo "  source .venv/bin/activate"