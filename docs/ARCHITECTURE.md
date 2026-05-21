# Architecture Overview

This repository serves as the GitHub profile and utility-code home for TBirdPIT.

## Layout

- `README.md`: profile-facing overview.
- `src/tbirdpit/`: reusable Python utilities.
- `tests/`: unit tests for package behavior.
- `.github/`: issue and pull request templates plus workflows.

## Python package design

The package is intentionally small and stable:

- `hello`: human-friendly smoke output.
- `load_json_config`: deterministic local config loading.
- `get_azure_environment_summary`: safe Azure context checks.
- `configure_logging`: shared logging defaults for scripts and demos.

## Quality model

- Ruff for linting and import order.
- Black for formatting.
- Pre-commit as the local gate.
- Pytest for behavior verification.
