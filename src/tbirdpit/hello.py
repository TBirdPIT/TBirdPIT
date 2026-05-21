"""Small utility module for local Python and Azure-oriented workflows."""

from __future__ import annotations

import argparse
import json
import logging
import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any


def hello(name: str, punctuation: str = "!") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}{punctuation}"


def load_json_config(path: str | Path) -> dict[str, Any]:
    """Load a JSON config file with clear error handling."""
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file was not found: {config_path}")

    try:
        return json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Config file is not valid JSON: {config_path}") from exc


def get_azure_environment_summary(
    env: Mapping[str, str] | None = None,
) -> dict[str, str | bool | None]:
    """Summarize key Azure environment values without exposing secrets."""
    environment = env or os.environ
    tenant_id = environment.get("AZURE_TENANT_ID")
    subscription_id = environment.get("AZURE_SUBSCRIPTION_ID")
    authority = environment.get("AZURE_AUTHORITY_HOST", "https://login.microsoftonline.us")

    return {
        "tenant_id": tenant_id,
        "subscription_id": subscription_id,
        "authority_host": authority,
        "is_azure_configured": bool(tenant_id and subscription_id),
    }


def configure_logging(level: str = "INFO", logger_name: str = "tbirdpit") -> logging.Logger:
    """Create a console logger with a stable format for local tooling."""
    logger = logging.getLogger(logger_name)
    logger.setLevel(level.upper())

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                datefmt="%Y-%m-%dT%H:%M:%S",
            )
        )
        logger.addHandler(handler)

    return logger


def main() -> None:
    """CLI entrypoint for quick local verification."""
    parser = argparse.ArgumentParser(description="TBirdPIT helper utilities")
    parser.add_argument("--name", default="Veteran Builder", help="Name used in greeting output")
    parser.add_argument("--config", help="Optional path to a JSON configuration file")
    parser.add_argument(
        "--azure-context",
        action="store_true",
        help="Print Azure environment summary",
    )
    args = parser.parse_args()

    logger = configure_logging()
    logger.info(hello(args.name))

    if args.config:
        config = load_json_config(args.config)
        logger.info("Loaded config with keys: %s", sorted(config.keys()))

    if args.azure_context:
        logger.info("Azure context: %s", get_azure_environment_summary())


if __name__ == "__main__":
    main()
