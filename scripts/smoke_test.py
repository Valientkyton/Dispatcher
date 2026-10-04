import time

from dispatcher.model import complete


messages = [
    {"role": "user", "content": "What is the capital of France?"}
]

started_at = time.perf_counter()
response = complete(messages)
elapsed = time.perf_counter() - started_at

usage = response.usage

print(f"Model: {response.model}")
print(f"Reply: {response.choices[0].message.content}")
print(
    "Tokens: "
    f"prompt={usage.prompt_tokens}, "
    f"completion={usage.completion_tokens}, "
    f"total={usage.total_tokens}"
)
print(f"Elapsed: {elapsed:.2f} seconds")