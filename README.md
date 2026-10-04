# Dispatcher

Dispatcher is a multi-agent SOC assistant that investigates security alerts. An orchestrator routes each alert or question to specialist agents for triage, detection engineering, threat intel and hunting, and every step they take is logged so any verdict can be replayed and audited. It's built on a from-scratch agent loop rather than an agent framework.

**Status:** early development. Currently building the agent core.

## Design

- **Models:** Gemma 4 through Ollama on Google Colab Pro. `gemma4:26b` (mixture-of-experts, fast) is the default; `gemma4:31b` (dense) handles the hardest tasks. Picked with the `DISPATCHER_PROFILE` environment variable. Small models were dropped because they were unreliable at multi-step tool use.
- **One door to the model:** every model call goes through `dispatcher/model.py`, so switching models or providers touches one file.
- **Testable without a GPU:** tests run against a scripted fake model, so paid GPU time is only spent on real model behavior.
- **Data:** only public datasets and synthetic fixtures, since model inputs pass through a cloud runtime.