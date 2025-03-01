from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class VerifyAccountRepositoryTypeError(Enum):
    INVALID_TOKEN = {"msg": "Verification token in invalid.", "code": 400}
    ALREADY_VERIFIED = {"msg": "The account is verified.", "code": 400}


class VerifyAccountRepositoryError(UserError):
    def __init__(self, error_type: VerifyAccountRepositoryTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
