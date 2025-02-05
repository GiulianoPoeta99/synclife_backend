from typing import Optional

from src.api.v1.reminder.domain.entities.reminder import Reminder
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)
from src.api.v1.reminder.domain.repositories.reminder_repository import (
    ReminderRepository,
)
from src.api.v1.shared.domain.value_objects import Uuid


class ReminderRepositoryValidator:
    @staticmethod
    def reminder_found(
        reminder: Optional[Reminder],
    ) -> Reminder:
        """
        Valida que un recordatorio exista. Si no existe, lanza una excepción.
        """
        if reminder is None:
            raise ReminderValidationError(
                ReminderValidationTypeError.REMINDER_NOT_FOUND
            )
        return reminder

    @staticmethod
    def user_owns_reminder(
        repository: ReminderRepository,
        user_id: Uuid,
        reminder_id: Uuid,
    ) -> None:
        """
        Valida que un recordatorio exista y que el usuario sea el propietario.
        Lanza una excepción si alguna de estas condiciones no se cumple.
        """
        reminder = ReminderRepositoryValidator.reminder_found(
            repository.find_by_id(reminder_id)
        )
        if reminder.user_id != user_id:
            raise ReminderValidationError(
                ReminderValidationTypeError.REMINDER_NOT_OWNED_BY_USER
            )
