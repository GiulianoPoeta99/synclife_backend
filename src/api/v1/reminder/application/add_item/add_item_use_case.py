from datetime import datetime, timezone

from src.api.v1.reminder.application.add_item.add_item_dto import AddReminderItemDto
from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)
from src.api.v1.reminder.domain.repositories import ReminderRepository
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class AddReminderItemUseCase:
    def __init__(self, repository: ReminderRepository, user_repository: UserRepository):
        self.repository = repository
        self.user_repository = user_repository

    def execute(self, dto: AddReminderItemDto) -> Reminder:
        # Valida si el usuario existe
        UserRepositoryValidator.user_found(
            self.user_repository.find_by_id(Uuid(dto.user_id))
        )

        # Obtener la fecha de creación (fecha actual)
        creation_date = datetime.now(timezone.utc)

        # Validar que la fecha de recordatorio no sea anterior a la fecha de creación
        if dto.remind_date < creation_date:
            raise ReminderValidationError(ReminderValidationTypeError.INVALID_DATE)

        # Crear el recordatorio
        reminder = Reminder(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            is_deleted=False,
            title=dto.title,
            content=dto.content,
            remind_date=dto.remind_date,
            updated_at=None,
        )
        print(f"Datos del recordatorio a guardar: {reminder}")

        # Intentar guardar el recordatorio
        is_saved, reminder_saved = self.repository.save(reminder)

        if not is_saved or reminder_saved is None:
            raise ReminderValidationError(ReminderValidationTypeError.SAVE_FAILED)

        return reminder_saved
