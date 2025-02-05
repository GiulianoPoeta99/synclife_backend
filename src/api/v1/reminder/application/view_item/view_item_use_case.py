from src.api.v1.reminder.application.view_item.view_item_dto import ViewReminderItemDto
from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.repositories.reminder_repository import (
    ReminderRepository,
)
from src.api.v1.reminder.domain.validators.reminder_repository_validator import (
    ReminderRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.repositories import UserRepository


class ViewReminderItemUseCase:
    def __init__(self, repository: ReminderRepository, user_repository: UserRepository):
        self.repository = repository
        self.user_repository = user_repository

    def execute(self, dto: ViewReminderItemDto) -> Reminder:
        # Validar que el usuario sea el propietario y que el recordatorio exista
        ReminderRepositoryValidator.user_owns_reminder(
            self.repository,
            Uuid(dto.user_id),
            Uuid(dto.reminder_id),
        )

        # Validar y obtener el recordatorio
        reminder = ReminderRepositoryValidator.reminder_found(
            self.repository.find_by_id(Uuid(dto.reminder_id))
        )

        return reminder
