# 0001: Model profiles

**Decision:** Three profiles in `config.py`, picked with `DISPATCHER_PROFILE`:
small = qwen3.5:4b, medium = qwen3.5:9b (default), large = qwen3.5:27b on Colab Pro (provisional).
All model calls go through `model.py`.

**Why:**  In an initial tool-calling test (5 runs each), the 4B called the tool 5/5 times at 3s warm; the 9B called it 5/5 at 4s warm.


**Revisit:** When the large model is chosen, and once the first full evaluation is done..