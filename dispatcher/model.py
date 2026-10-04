from openai import OpenAI

from . import config


client = OpenAI(
    base_url=config.OLLAMA_BASE_URL,
    api_key="ollama",
)


def complete(messages, tools=None):
    model = config.get_active_model()

    if tools:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
        )

    return client.chat.completions.create(
        model=model,
        messages=messages,
    )