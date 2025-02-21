from enum import Enum
from typing import Dict, cast

from src.api.shared.domain.errors.shared_error import SharedError


class UuidTypeError(Enum):
    INVALID_UUID = {"msg": "La UUID no es válida.", "code": 400}


class UuidError(SharedError):
    def __init__(self, error_type: UuidTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
