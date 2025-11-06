from fastapi import APIRouter, Request, HTTPException, Depends
from pydantic import BaseModel
from config import settings
from services.openai_service import generate as openai_generate
from services.ollama_service import generate as ollama_generate
from utils.logger import logger


router = APIRouter()


class Message(BaseModel):
    role: str
content: str


class ChatRequest(BaseModel):
    messages: list[Message]
params: dict | None = None


@router.post('/chat')
async def chat_endpoint(req: ChatRequest, request: Request):
    if not req.messages:
    raise HTTPException(status_code=400, detail='messages_required')


override = (request.headers.get('x-backend') or request.query_params.get('backend') or '').lower()
backend = override or settings.default_backend
logger.info(f'Routing request to backend={backend}')


if backend == 'ollama':
    result = await ollama_generate(req.messages, req.params or {})
else:
    result = await openai_generate(req.messages, req.params or {})


return {'backend': backend, 'result': result}