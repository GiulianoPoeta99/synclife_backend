"""
Module that defines errors associated with operations in the user repository.

This module contains:
  - UserRepositoryTypeError: Enumeration that specifies the types of errors related to
                             user management in the repository, such as an already
                             existing user, user not found, or a failed operation.
  - UserRepositoryError: Exception raised when an error occurs in user repository
                         operations.
"""

from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class UserRepositoryTypeError(Enum):
    """
    Enumeration of error types related to user repositories.

    Each member of this enumeration contains a dictionary that defines a descriptive
    message and an error code associated with specific failures in repository
    operations.

    Attributes:
        USER_ALREADY_EXISTS (Dict[str, int | str]): Indicates that a user with the same
                                                    email already exists.
        USER_NOT_FOUND (Dict[str, int | str]): Indicates that the user is not
                                               registered.
        OPERATION_FAILED (Dict[str, int | str]): Indicates that the operation failed.
    """

    USER_ALREADY_EXISTS = {"msg": "A user with this email already exists.", "code": 400}
    USER_NOT_FOUND = {"msg": "The user is not registered.", "code": 400}
    OPERATION_FAILED = {"msg": "The operation failed.", "code": 400}


class UserRepositoryError(UserError):
    """
    Exception raised when an error occurs in user repository operations.

    This exception inherits from UserError and is initialized using a value from
    UserRepositoryTypeError, thereby setting the corresponding descriptive message and
    error code.

    Args:
        error_type (UserRepositoryTypeError): Specific error type related to user
                                              management in the repository.
    """

    def __init__(self, error_type: UserRepositoryTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
