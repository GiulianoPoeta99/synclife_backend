from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class PasswordTypeError(Enum):
    TOO_SHORT = {"msg": "La contraseña debe tener al menos 8 caracteres.", "code": 400}
    MISSING_NUMBER = {
        "msg": "La contraseña debe contener al menos un número.",
        "code": 400,
    }
    MISSING_UPPERCASE = {
        "msg": "La contraseña debe contener al menos una letra mayúscula.",
        "code": 400,
    }
    MISSING_LOWERCASE = {
        "msg": "La contraseña debe contener al menos una letra minúscula.",
        "code": 400,
    }
    MISSING_SPECIAL = {
        "msg": "La contraseña debe contener al menos un carácter especial.",
        "code": 400,
    }
    WEAK_PASSWORD = {"msg": "La contraseño es demasiade debíl.", "code": 400}


class PasswordError(UserError):
    def __init__(self, error_type: PasswordTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
