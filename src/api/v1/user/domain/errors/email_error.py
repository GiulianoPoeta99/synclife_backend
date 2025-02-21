from enum import Enum
from typing import Dict, cast

from src.api.v1.user.domain.errors.user_error import UserError


class EmailTypeError(Enum):
    INVALID_EMAIL = {"msg": "El correo electrónico no es válido.", "code": 400}


class EmailError(UserError):
    def __init__(self, error_type: EmailTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
