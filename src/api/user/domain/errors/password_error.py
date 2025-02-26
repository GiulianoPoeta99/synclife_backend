"""
Module that defines the errors associated with handling passwords in the user domain.

This module contains:
  - PasswordTypeError: An enumeration that specifies the different types of errors in
                       password validation,each with a descriptive message and an error
                       code.
  - PasswordError: Exception raised when a specific error occurs in password validation.
"""

from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class PasswordTypeError(Enum):
    """
    Enumeration of error types related to password validation.

    Each member of this enumeration contains a dictionary with a descriptive message
    and an error code associated with a failure in password validation.

    Attributes:
        TOO_SHORT (Dict[str, int | str]): The password must be at least 8 characters
                                          long.
        MISSING_NUMBER (Dict[str, int | str]): The password must contain at least one
                                               number.
        MISSING_UPPERCASE (Dict[str, int | str]): The password must contain at least one
                                                  uppercase letter.
        MISSING_LOWERCASE (Dict[str, int | str]): The password must contain at least one
                                                  lowercase letter.
        MISSING_SPECIAL (Dict[str, int | str]): The password must contain at least one
                                                special character.
        WEAK_PASSWORD (Dict[str, int | str]): The password is too weak.
    """

    TOO_SHORT = {"msg": "The password must be at least 8 characters long.", "code": 400}
    MISSING_NUMBER = {
        "msg": "The password must contain at least one number.",
        "code": 400,
    }
    MISSING_UPPERCASE = {
        "msg": "The password must contain at least one uppercase letter.",
        "code": 400,
    }
    MISSING_LOWERCASE = {
        "msg": "The password must contain at least one lowercase letter.",
        "code": 400,
    }
    MISSING_SPECIAL = {
        "msg": "The password must contain at least one special character.",
        "code": 400,
    }
    WEAK_PASSWORD = {"msg": "The password is too weak.", "code": 400}


class PasswordError(UserError):
    """
    Exception raised when an error related to password validation occurs.

    This exception inherits from UserError and is initialized using a value from
    PasswordTypeError, thus setting the corresponding descriptive message and error
    code.

    Args:
        error_type (PasswordTypeError): Specific error type related to password
                                        validation.
    """

    def __init__(self, error_type: PasswordTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
