flowchart LR
A[Client] -->|POST /api/ai/chat| B[API Gateway (FastAPI)]
B --> C{choose backend}
C -->|openai| D[OpenAI Adapter]
C -->|ollama| E[Ollama Adapter]
D --> F[OpenAI API]
E --> G[Local Ollama Server]
subgraph Future Modules
H[Memory]
I[Voice]
J[Image]
end
B --> H
B --> I
B --> J