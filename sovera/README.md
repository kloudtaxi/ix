

# Getting Started - Sovera-ix



> This is a fork of [ix](https://github.com/kreneskyp/ix.git) for integration with Sovera Platform. Anything in this branch should be considered as `out-off-tree` from the `ix origin`. 

> :pray:  As always please don't leave any **API KEYs, Tokens, Credentials** or other sensitive information in this file. 

> :reminder_ribbon:  **TODO**
>
> - [ ] Implement pre-commit hook to reject files with sensitive information. 

---



## Dev Deployment

- [ ] **TODO:** write detailed dev documentation. This is too terse for devs without DevOps experience. 

   

1. Update .env with required `keys` and `endpoints`
2. From root of the project run `make dev_setup`  🙌  don't worry if you see a :shit: ton of errors. 
3. Bring the cluster down `make down`
4. Bring up dev_cluster `make cluster`



:eyes: at `Makefile` in project root for additional commands including DB migrations 

:tipping_hand_man: depending on the version of docker you many need to modify `Makefile` for docker compose to work. **Notice** the removal of hyphen in docker compose command

If your system has Docker Compose V2 installed instead of V1, use `docker compose` instead of `docker-compose`. Check if this is the case by running `$ docker compose version`. 

Example: 

```makefile
-LOAD_FIXTURE = docker-compose exec -T web ./manage.py loaddata
+LOAD_FIXTURE = docker compose exec -T web ./manage.py loaddata
```





## Configuration Reference

### `.env`

```shell
# ==================================================================
# REQUIRED SETUP:
#
# 1. copy this file to ".env" and fill in the values.
#    all values in this file are loaded into the environment
#    for web and agent workers.
#
# 2. Restart containers after making changes.
#
# Values in this file will be used if not set for Chains via UX or API
# ==================================================================

# Docker Compose env var to name the project.
# COMPOSE_PROJECT_NAME=sovera-agent-ix

# OpenAI is the default LLM used by predefined agents.
OPENAI_API_KEY=
# OPENAI_API_BASE=https://llama-gateway.sovera.xyz
#OPENAI_PROXY=http://localhost:8040


# ==================================================================
# OPTIONAL SETUP:
#
# These values are only required when using the corresponding
# features.
# ==================================================================

# LangSmith logging (requires a LangSmith account)
# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
# LANGCHAIN_API_KEY=
# LANGCHAIN_PROJECT=default

# llms
GOOGLE_API_KEY=
ANTHROPIC_API_KEY=

# Pinecone
PINECONE_API_KEY=
PINECONE_ENV=

# search
GOOGLE_API_KEY=
GOOGLE_CX_ID=
WOLFRAM_APP_ID=

# METAPHOR
METAPHOR_API_KEY=
```



### `ix/server/settings.py`

Added reverse proxy and dns name to allowed hosts configuration block. 

```python
# sinppet 

ALLOWED_HOSTS = [
     "localhost",
     "0.0.0.0",
     "127.0.0.1",
+    "138.197.78.223",
+    "ix.sovera.xyz",
 ]
```
