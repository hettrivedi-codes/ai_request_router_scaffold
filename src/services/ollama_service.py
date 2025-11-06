import httpx
from config import settings
from utils.logger import logger

async def generate(messages, params: dict):
    model = params.get("model") or settings.ollama_model
    prompt = "\n".join(f"{m.role}: {m.content}" for m in messages)
    url = f"{settings.ollama_url}/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": params.get("max_tokens", 1024),
        "temperature": params.get("temperature", 0.7),
    }

    async with httpx.AsyncClient(timeout=settings.ollama_timeout_ms / 1000) as client:
        resp = await client.post(url, json=payload)

    if resp.is_error:
        logger.error("Ollama error: %s", resp.text)
        raise RuntimeError("Ollama request failed")

    data = resp.json()
    text = data.get("output") or (data[0] if isinstance(data, list) else None)
    return {"raw": data, "text": text}
