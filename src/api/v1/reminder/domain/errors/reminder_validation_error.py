from enum import Enum

from src.api.v1.reminder.domain.errors.reminder_error import ReminderError


class ReminderValidationTypeError(Enum):
    REMINDER_NOT_FOUND = "El recordatorio no fue encontrado."
    REMINDER_DELETE_FAILED = "No se pudo eliminar el recordatorio."
    REMINDER_UPDATE_FAILED = "No se pudo modificar el recordatorio."
    REMINDER_SAVE_FAILED = "No se pudo crear el recordatorio."
    REMINDER_TITLE_INVALID = "El nombre del recordatorio no puede ser nulo."
    REMINDER_NOT_OWNED_BY_USER = "Este recordatorio no pertenece al usuario."
    REMINDER_DATE_INVALID = (
        "La fecha del recordatorio es inválida, debe ser posterior a la fecha actual."
    )
    NO_REMINDERS_FOUND = "No se encuentran recordatorios para el usuario"


class ReminderValidationError(ReminderError):
    def __init__(self, error_type: ReminderValidationTypeError):
        super().__init__(error_type.value)
