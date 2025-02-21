from enum import Enum
from typing import Dict, cast

from src.api.v1.user.domain.errors.user_error import UserError


class FullNameTypeError(Enum):
    INVALID_NAME = {"msg": "El nombre o apellido no es válido.", "code": 400}
    INVALID_NAME_FORMAT = {
        "msg": "El nombre o apellido tiene caracteres inválidos.",
        "code": 400,
    }
    NAME_TOO_LONG = {"msg": "El nombre o apellido es demasiado largo.", "code": 400}


class FullNameError(UserError):
    def __init__(self, error_type: FullNameTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
