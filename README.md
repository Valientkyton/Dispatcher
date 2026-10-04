# Dispatcher

Dispatcher is a multi-agent SOC assistant that investigates security alerts. An orchestrator routes each alert or question to specialist agents for triage, detection engineering, threat intel and hunting, and every step they take is logged so any verdict can be replayed and audited. It runs on local LLMs through Ollama, with hosted models as an option, and it's built on a from-scratch agent loop rather than an agent framework.

**Status:** early development. Currently building the agent core (Phase 1).