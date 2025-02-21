from enum import Enum
from typing import Dict, cast

from src.api.v1.reminder.domain.errors.reminder_error import ReminderError


class ReminderValidationTypeError(Enum):
    REMINDER_NOT_FOUND = {"msg": "El recordatorio no fue encontrado.", "code": 400}
    REMINDER_DELETE_FAILED = {
        "msg": "No se pudo eliminar el recordatorio.",
        "code": 400,
    }
    REMINDER_UPDATE_FAILED = {
        "msg": "No se pudo modificar el recordatorio.",
        "code": 400,
    }
    REMINDER_SAVE_FAILED = {"msg": "No se pudo crear el recordatorio.", "code": 400}
    REMINDER_TITLE_INVALID = {
        "msg": "El nombre del recordatorio no puede ser nulo.",
        "code": 400,
    }
    REMINDER_NOT_OWNED_BY_USER = {
        "msg": "Este recordatorio no pertenece al usuario.",
        "code": 400,
    }
    REMINDER_DATE_INVALID = {
        "msg": "La fecha del recordatorio debe ser mayor a la fecha actual.",
        "code": 400,
    }
    NO_REMINDERS_FOUND = {
        "msg": "No se encuentran recordatorios para el usuario",
        "code": 400,
    }


class ReminderValidationError(ReminderError):
    def __init__(self, error_type: ReminderValidationTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
