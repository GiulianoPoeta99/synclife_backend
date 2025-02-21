from .fastapi_note_routes import router as note_router
from .fastapi_tags_routes import router as tag_router

__all__ = ["note_router", "tag_router"]
