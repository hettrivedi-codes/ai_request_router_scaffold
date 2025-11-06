from fastapi import FastAPI
from config import settings
from routes.ai_router import router as ai_router
import uvicorn

app = FastAPI(title="AI Backend Scaffold (FastAPI)")
app.include_router(ai_router, prefix="/api/ai")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=settings.port, reload=True)
