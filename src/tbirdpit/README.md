# tbirdpit package

Small Python utilities for day-to-day developer workflows with a focus on secure Azure-oriented setup checks.

## Installation

```bash
pip install -e .
```

## What it includes

- `hello(name)` for friendly output checks.
- `load_json_config(path)` for safe JSON config loading with clear errors.
- `get_azure_environment_summary()` to verify required Azure environment context without printing secrets.
- `configure_logging()` for consistent console logging.

## Usage examples

```python
from tbirdpit import (
    configure_logging,
    get_azure_environment_summary,
    hello,
    load_json_config,
)

logger = configure_logging(level="INFO")
logger.info(hello("Engineer"))

settings = load_json_config("local.config.json")
logger.info("Loaded settings keys: %s", list(settings))

summary = get_azure_environment_summary()
logger.info("Azure summary: %s", summary)
```

## CLI demo

```bash
tbirdpit --name "Veteran Builder" --azure-context
```

With config loading:

```bash
tbirdpit --config ./sample.config.json --azure-context
```
