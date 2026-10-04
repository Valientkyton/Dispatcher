import pytest

from dispatcher import config


def test_default_profile_is_standard(monkeypatch):
    monkeypatch.delenv(config.PROFILE_ENV_VAR, raising=False)

    assert config.get_active_model() == "gemma4:26b"


def test_max_profile(monkeypatch):
    monkeypatch.setenv(config.PROFILE_ENV_VAR, "max")

    assert config.get_active_model() == "gemma4:31b"


def test_unknown_profile_raises_error(monkeypatch):
    monkeypatch.setenv(config.PROFILE_ENV_VAR, "made_up")

    with pytest.raises(ValueError, match="Valid profiles"):
        config.get_active_model()