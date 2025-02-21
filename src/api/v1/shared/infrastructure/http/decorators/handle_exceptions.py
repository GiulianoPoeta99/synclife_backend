from typing import Any, Awaitable, Callable, TypeVar

from fastapi import HTTPException

from src.api.v1.inventory.domain.errors import InventoryItemError
from src.api.v1.notes.domain.errors.notes import NoteError
from src.api.v1.notes.domain.errors.tags import TagError
from src.api.v1.reminder.domain.errors import ReminderValidationError
from src.api.v1.shared.domain.errors.shared_error import SharedError
from src.api.v1.user.domain.errors.user_error import UserError

T = TypeVar("T")


def handle_exceptions(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
    async def wrapper(*args: Any, **kwargs: Any) -> T:
        try:
            return await func(*args, **kwargs)
        except (
            SharedError,
            UserError,
            NoteError,
            InventoryItemError,
            TagError,
            ReminderValidationError,
        ) as e:
            detail = str(e)
            code = int(e.code)
            raise HTTPException(status_code=code, detail=detail)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error interno del servidor: {e}"
            )

    return wrapper
