"""
Module that defines errors associated with handling phone numbers in the user
domain.

This module contains:
  - PhoneTypeError: Enumeration that specifies the error related to an invalid phone
                    number.
  - PhoneError: Exception raised when an error in phone number validation is detected.
"""

from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class PhoneTypeError(Enum):
    """
    Enumeration of error types related to phone numbers.

    Each member of this enumeration contains a dictionary with a descriptive message
    and an error code associated with the failure in phone number validation.

    Attributes:
        INVALID_PHONE (Dict[str, int | str]): Indicates that the phone number is not
                                              valid.
    """

    INVALID_PHONE = {"msg": "The phone number is not valid.", "code": 400}


class PhoneError(UserError):
    """
    Exception raised when an error in phone number validation occurs.

    This exception inherits from UserError and is initialized using a value from
    PhoneTypeError, thus setting the corresponding descriptive message and error code.

    Args:
        error_type (PhoneTypeError): Specific error type related to phone number
                                     validation.
    """

    def __init__(self, error_type: PhoneTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
