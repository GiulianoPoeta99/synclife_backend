"""
Module that defines the errors associated with handling email addresses in the user
domain.

This module contains:
  - EmailTypeError: Enumeration of specific email errors, with a message and code.
  - EmailError: Exception raised when an error related to email occurs.
"""

from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class EmailTypeError(Enum):
    """
    Enumeration of error types related to email addresses.

    Each member of this enumeration encapsulates a descriptive message and an error code
    that is used to identify specific errors in email validation.

    Attributes:
        INVALID_EMAIL (Dict[str, int | str]): Error indicating that the email address
                                              is not valid, with a descriptive message
                                              and an error code (400).
    """

    INVALID_EMAIL = {"msg": "The email address is not valid.", "code": 400}


class EmailError(UserError):
    """
    Exception raised when an error related to email occurs.

    This exception inherits from UserError and is initialized using a value from
    EmailTypeError, which allows setting the corresponding message and error code.

    Args:
        error_type (EmailTypeError): The type of error that occurred during email
                                     validation.
    """

    def __init__(self, error_type: EmailTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
