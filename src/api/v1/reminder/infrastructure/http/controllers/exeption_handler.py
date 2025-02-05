from typing import Any, Awaitable, Callable, TypeVar

from fastapi import HTTPException

from src.api.v1.reminder.domain.errors import ReminderValidationError
from src.api.v1.shared.domain.errors.shared_error import SharedError

T = TypeVar("T")


def handle_exceptions(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
    """Decorador para manejar excepciones específicas de Reminder y generales."""

    async def wrapper(*args: Any, **kwargs: Any) -> T:
        try:
            return await func(*args, **kwargs)
        except (ReminderValidationError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error interno del servidor: {e}"
            )

    return wrapper
