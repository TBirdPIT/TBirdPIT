import logging
import tempfile
from pathlib import Path

import pytest

from tbirdpit.hello import (
    configure_logging,
    get_azure_environment_summary,
    hello,
    load_json_config,
)


def test_hello_default_punctuation() -> None:
    assert hello("DevOps") == "Hello, DevOps!"


def test_load_json_config_success() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        config_file = Path(temp_dir) / "config.json"
        config_file.write_text('{"mode": "local", "debug": true}', encoding="utf-8")

        config = load_json_config(config_file)

    assert config["mode"] == "local"
    assert config["debug"] is True


def test_load_json_config_invalid_json() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        config_file = Path(temp_dir) / "invalid.json"
        config_file.write_text('{"mode": "local",}', encoding="utf-8")

        with pytest.raises(ValueError):
            load_json_config(config_file)


def test_get_azure_environment_summary_detects_configuration() -> None:
    env = {
        "AZURE_TENANT_ID": "tenant",
        "AZURE_SUBSCRIPTION_ID": "subscription",
        "AZURE_AUTHORITY_HOST": "https://login.microsoftonline.us",
    }

    summary = get_azure_environment_summary(env)

    assert summary["is_azure_configured"] is True
    assert summary["authority_host"] == "https://login.microsoftonline.us"


def test_configure_logging_reuses_existing_logger() -> None:
    logger = configure_logging(level="INFO", logger_name="tbirdpit.test")
    handler_count = len(logger.handlers)

    logger_again = configure_logging(level="DEBUG", logger_name="tbirdpit.test")

    assert logger is logger_again
    assert len(logger_again.handlers) == handler_count
    assert logger_again.level == logging.DEBUG
