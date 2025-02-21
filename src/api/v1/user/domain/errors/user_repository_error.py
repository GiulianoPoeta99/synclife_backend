from enum import Enum
from typing import Dict, cast

from src.api.v1.user.domain.errors.user_error import UserError


class UserRepositoryTypeError(Enum):
    USER_ALREADY_EXISTS = {"msg": "El usuario con este email ya existe.", "code": 400}
    USER_NOT_FOUND = {"msg": "El usuario no esta registrado.", "code": 400}
    OPERATION_FAILED = {"msg": "La operación fallo.", "code": 400}


class UserRepositoryError(UserError):
    def __init__(self, error_type: UserRepositoryTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
