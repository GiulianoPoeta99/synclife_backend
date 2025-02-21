from enum import Enum
from typing import Dict, cast

from src.api.v1.user.domain.errors.user_error import UserError


class UserValidationTypeError(Enum):
    INVALID_BIRTHDATE = {"msg": "La fecha de nacimiento no es válida.", "code": 400}
    INVALID_CREDENTIALS = {
        "msg": "El email o la contraseña son incorrectos.",
        "code": 400,
    }


class UserValidationError(UserError):
    def __init__(self, error_type: UserValidationTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
