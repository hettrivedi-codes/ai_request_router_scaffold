import httpx
from config import settings
from utils.logger import logger


async def generate(messages, params: dict):
model = params.get('model') or settings.ollama_model
url = f"{settings.ollama_url}/api/generate"


# Convert messages to a single prompt (adapter responsibility)
prompt = '
'.join([f"{m.role}: {m.content}" for m in messages])


payload = {
'model': model,
'prompt': prompt,
'max_tokens': params.get('max_tokens', 1024),
'temperature': params.get('temperature', 0.7),
}


async with httpx.AsyncClient(timeout=settings.ollama_timeout_ms / 1000.0) as client:
resp = await client.post(url, json=payload)


if resp.status_code >= 400:
    logger.error('Ollama error', resp.text)
raise RuntimeError('Ollama request failed')


data = resp.json()
# Ollama shapes vary; try common keys
text = data.get('output') or (data[0] if isinstance(data, list) and data else None)


return { 'raw': data, 'text': text }