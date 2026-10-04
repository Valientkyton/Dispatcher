import os


OLLAMA_BASE_URL = "http://localhost:11434/v1"

MODEL_PROFILES = {
    "small": "qwen3.5:4b",
    "medium": "qwen3.5:9b",
    "large": "qwen3.5:27b",
}

DEFAULT_PROFILE = "medium"
PROFILE_ENV_VAR = "DISPATCHER_PROFILE"


def get_active_model() -> str:
    profile = os.environ.get(PROFILE_ENV_VAR, DEFAULT_PROFILE)

    if profile not in MODEL_PROFILES:
        valid_profiles = ", ".join(MODEL_PROFILES)
        raise ValueError(
            f"Unknown profile {profile!r}. Valid profiles: {valid_profiles}"
        )

    return MODEL_PROFILES[profile]