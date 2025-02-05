from src.api.v1.reminder.application.modify_item.modify_item_dto import (
    ModifyReminderItemDto,
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
from src.api.v1.reminder.domain.validators.reminder_validator import ReminderValidator
from src.api.v1.shared.domain.value_objects import Uuid


class ModifyReminderItemUseCase:
    def __init__(self, repository: ReminderRepository):
        self.repository = repository

    def execute(self, dto: ModifyReminderItemDto) -> Reminder:
        # Validar que el usuario sea el propietario y que el recordatorio exista
        ReminderRepositoryValidator.user_owns_reminder(
            self.repository,
            Uuid(dto.user_id),
            Uuid(dto.reminder_id),
        )

        # Valido todo
        ReminderValidator.validate_all(dto.title, dto.remind_date)

        # Validar que el recordatorio exista
        reminder = ReminderRepositoryValidator.reminder_found(
            self.repository.find_by_id(Uuid(dto.reminder_id))
        )

        # Actualizar los campos del recordatorio
        reminder.title = dto.title
        reminder.content = dto.content
        reminder.remind_date = dto.remind_date

        # Guardar los cambios
        is_modified, reminder_modified = self.repository.update(reminder)
        if not is_modified or reminder_modified is None:
            raise ReminderValidationError(
                ReminderValidationTypeError.REMINDER_UPDATE_FAILED
            )

        return reminder_modified
