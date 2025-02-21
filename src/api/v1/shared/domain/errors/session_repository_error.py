from enum import Enum
from typing import Dict, cast

from src.api.v1.shared.domain.errors.shared_error import SharedError


class SessionRepositoryTypeError(Enum):
    INVALID_USER = {"msg": "No tenés permisos para hacer esto.", "code": 403}
    INVALID_SESSION = {"msg": "Sesión inválida o expirada", "code": 401}


class SessionRepositoryError(SharedError):
    def __init__(self, error_type: SessionRepositoryTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
