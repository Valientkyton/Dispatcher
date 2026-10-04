# 0002: Isolated environment for the AI dev assistant

**Decision:** The AI dev assistant runs in a dedicated WSL2 Ubuntu with no access to the Windows drive, Windows programs or GitHub credentials. Its tools run in a Docker sandbox with no network and read-only access to a copy of the code, web and elevated tools are disabled, and its gateway listens only on localhost.

**Why:** The assistant reads code, logs and documents that could contain prompt injections. Isolation means a successful injection can't modify the project, reach personal files, push to GitHub or send data out. In testing, the local model ignored a "stop and ask" instruction in two out of two tries, so these limits are enforced by the environment rather than by instructions to the model.

**Revisit:** If the assistant needs a new capability, like web access or writing code, grant that one capability narrowly instead of loosening the sandbox as a whole.