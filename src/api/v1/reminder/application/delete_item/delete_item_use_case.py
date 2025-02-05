from src.api.v1.reminder.application.delete_item.delete_item_dto import (
    DeleteReminderItemDto,
)
from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)
from src.api.v1.reminder.domain.repositories import ReminderRepository
from src.api.v1.reminder.domain.validators.reminder_repository_validator import (
    ReminderRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class DeleteReminderItemUseCase:
    def __init__(self, repository: ReminderRepository):
        self.repository = repository

    def execute(self, dto: DeleteReminderItemDto) -> Reminder:
        # Validar que el usuario sea el propietario y que el recordatorio exista
        ReminderRepositoryValidator.user_owns_reminder(
            self.repository,
            Uuid(dto.user_id),
            Uuid(dto.reminder_id),
        )

        # Buscar y validar el recordatorio
        reminder = ReminderRepositoryValidator.reminder_found(
            self.repository.find_by_id(Uuid(dto.reminder_id))
        )

        # Eliminar el recordatorio
        is_deleted, reminder_deleted = self.repository.delete(reminder)
        if not is_deleted or reminder_deleted is None:
            raise ReminderValidationError(
                ReminderValidationTypeError.REMINDER_DELETE_FAILED
            )

        return reminder_deleted
