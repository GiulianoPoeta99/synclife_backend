"""
Module that defines the errors associated with handling full names in the user domain.

This module contains:
  - FullNameTypeError: Enumeration of error types related to the validation of full
                       names.
  - FullNameError: Exception raised when a specific error occurs during the validation
                   of a full name.
"""

from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class FullNameTypeError(Enum):
    """
    Enumeration of error types for full names.

    Each member of this enumeration contains a dictionary with a descriptive message
    and an error code, which is used to identify specific errors during the validation
    of first and last names.

    Attributes:
        INVALID_NAME (Dict[str, int | str]): Indicates that the first name or last name
                                             is not valid.
        INVALID_NAME_FORMAT (Dict[str, int | str]): Indicates that the first name or
                                                    last name contains invalid
                                                    characters.
        NAME_TOO_LONG (Dict[str, int | str]): Indicates that the first name or last name
                                              is too long.
    """

    INVALID_NAME = {"msg": "The first name or last name is not valid.", "code": 400}
    INVALID_NAME_FORMAT = {
        "msg": "The first name or last name contains invalid characters.",
        "code": 400,
    }
    NAME_TOO_LONG = {"msg": "The first name or last name is too long.", "code": 400}


class FullNameError(UserError):
    """
    Exception raised when an error related to full name validation occurs.

    This exception inherits from UserError and is initialized using a value from
    FullNameTypeError, which sets the corresponding error message and error code.

    Args:
        error_type (FullNameTypeError): Specific error type related to full name
                                        validation.
    """

    def __init__(self, error_type: FullNameTypeError):
        """
        Initializes the FullNameError exception using an error type defined in
        FullNameTypeError.

        Args:
            error_type (FullNameTypeError): The type of error that occurred during
                                            validation.
        """
        super().__init__(cast(Dict[str, str | int], error_type.value))
