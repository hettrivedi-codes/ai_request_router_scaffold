# AI Backend Scaffold


## Setup
1. Copy `.env.example` to `.env` and fill API keys.
2. `npm install`
3. `npm run start` or `docker-compose up --build`


## Usage
POST /api/ai/chat
Content-Type: application/json


Body:
{
"messages": [ { "role": "system", "content": "You are a helpful assistant." }, {"role":"user","content":"Hello"} ],
"params": { "temperature": 0.5 }
}


To force Ollama for a single request, send header `x-backend: ollama` or `?backend=ollama`.


## Next steps
- Add authentication (API keys / JWT)
- Add rate-limiting and request logging
- Add structured tests for adapters and router
- Add memory module for context persistence
- Add voice + image processing modules