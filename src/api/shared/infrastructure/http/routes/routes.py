from typing import Any

from fastapi import APIRouter, Header, HTTPException

from src.api.inventory.infrastructure.http.routes import inventory_router
from src.api.notes.infrastructure.http.routes import note_router, tag_router
from src.api.reminder.infrastructure.http.routes import reminder_router
from src.api.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
)
from src.api.user.infrastructure.http.routes import user_router

router: APIRouter = APIRouter()

router.include_router(user_router)
router.include_router(inventory_router)
router.include_router(note_router)
router.include_router(tag_router)
router.include_router(reminder_router)


@router.get("/check/validate-session", summary="Valida si la sesión es válida")
async def validate_session(session_token: str = Header(...)) -> dict[str, Any]:
    """
    Endpoint para validar si una sesión es válida.
    """
    session_repository = InMemorySessionRepository.get_repository()
    user_id = session_repository.get_user_from_session(session_token)

    if not user_id:
        raise HTTPException(status_code=401, detail="Sesión inválida o expirada")
    return {"valid": True, "user_id": user_id}
