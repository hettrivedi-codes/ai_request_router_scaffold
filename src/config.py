from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    port: int = 8000
default_backend: str = 'openai' # or 'ollama'


openai_api_key: str | None = None
openai_model: str = 'gpt-4o-mini'


ollama_url: AnyHttpUrl = 'http://localhost:11434'
ollama_model: str = 'llama2'
ollama_timeout_ms: int = 30000


class Config:
    env_file = '.env'
env_file_encoding = 'utf-8'


settings = Settings()