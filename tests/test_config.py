import pytest

from dispatcher import config


def test_default_profile_is_medium(monkeypatch):
    monkeypatch.delenv(config.PROFILE_ENV_VAR, raising=False)

    assert config.get_active_model() == "qwen3.5:9b"


def test_small_profile(monkeypatch):
    monkeypatch.setenv(config.PROFILE_ENV_VAR, "small")

    assert config.get_active_model() == "qwen3.5:4b"


def test_unknown_profile_raises_error(monkeypatch):
    monkeypatch.setenv(config.PROFILE_ENV_VAR, "made_up")

    with pytest.raises(ValueError, match="Valid profiles"):
        config.get_active_model()