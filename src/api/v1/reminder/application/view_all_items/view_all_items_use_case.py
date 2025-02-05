from typing import List

from src.api.v1.reminder.application.view_all_items.view_all_items_dto import (
    ViewAllReminderItemsDto,
)
from src.api.v1.reminder.domain.entities.reminder import Reminder
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)
from src.api.v1.reminder.domain.repositories.reminder_repository import (
    ReminderRepository,
)


class ViewAllReminderItemsUseCase:
    def __init__(self, repository: ReminderRepository):
        self.repository = repository

    def execute(self, dto: ViewAllReminderItemsDto) -> List[Reminder]:
        # Buscar todos los recordatorios del usuario
        reminders = self.repository.find_all_by_user_id(dto.user_id)

        # Lanzar error si no hay recordatorios
        if not reminders:
            raise ReminderValidationError(
                ReminderValidationTypeError.NO_REMINDERS_FOUND
            )

        # Retornar los recordatorios
        return reminders
