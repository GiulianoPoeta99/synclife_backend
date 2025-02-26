"""
Module that defines validation errors in the user domain.

This module contains:
  - UserValidationTypeError: Enumeration that defines the types of errors related
                              to user data validation.
  - UserValidationError: Exception that is raised when an error occurs during the
                         validation of a user's data.
"""

from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class UserValidationTypeError(Enum):
    """
    Enumeration of user validation error types.

    Each member of this enumeration contains a dictionary with a descriptive message
    and an error code, which is used to identify specific errors in the validation
    of user data.

    Attributes:
        INVALID_BIRTHDATE (Dict[str, int | str]): Indicates that the birthdate is not
                                                  valid.
        INVALID_CREDENTIALS (Dict[str, int | str]): Indicates that the email or password
                                                    is incorrect.
    """

    INVALID_BIRTHDATE = {"msg": "The birthdate is not valid.", "code": 400}
    INVALID_CREDENTIALS = {
        "msg": "The email or password is incorrect.",
        "code": 400,
    }


class UserValidationError(UserError):
    """
    Exception that is raised when an error occurs during the validation of a user's
    data.

    This exception inherits from UserError and is initialized using a value from
    UserValidationTypeError, thereby setting the corresponding descriptive message and
    error code.

    Args:
        error_type (UserValidationTypeError): Specific error type related to user
                                              validation.
    """

    def __init__(self, error_type: UserValidationTypeError):
        """
        Initializes the UserValidationError exception.

        Args:
            error_type (UserValidationTypeError): The type of error that occurred during
                                                  validation.
        """
        super().__init__(cast(Dict[str, str | int], error_type.value))
