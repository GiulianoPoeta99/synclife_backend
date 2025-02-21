from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.shared.infrastructure.http.routes import base_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Permite todos los orígenes, pero en producción deberías restringirlo
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)

app.include_router(base_router, prefix="/api")
