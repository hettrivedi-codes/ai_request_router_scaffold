import httpx
from config import settings
from utils.logger import logger

OPENAI_CHAT_URL = "https://api.openai.com/v1/chat/completions"

async def generate(messages, params: dict):
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY not configured")

    payload = {
        "model": params.get("model") or settings.openai_model,
        "messages": [m.model_dump() for m in messages],
        "temperature": params.get("temperature", 0.7),
        "max_tokens": params.get("max_tokens", 1024),
    }

    headers = {
        "Authorization": f"Bearer {settings.openai_api_key}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(OPENAI_CHAT_URL, json=payload, headers=headers, timeout=30.0)

    if resp.is_error:
        logger.error("OpenAI error: %s", resp.text)
        raise RuntimeError("OpenAI request failed")

    data = resp.json()
    text = data.get("choices", [{}])[0].get("message", {}).get("content")
    return {"raw": data, "text": text}
