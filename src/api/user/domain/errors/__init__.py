"""
Initialization module for user domain errors.

This module imports and exposes the exceptions and enumerations associated with errors
in the user domain, including errors for:
  - Email (EmailError, EmailTypeError)
  - FullName (FullNameError, FullNameTypeError)
  - Password (PasswordError, PasswordTypeError)
  - Phone (PhoneError, PhoneTypeError)
  - User Validation (UserValidationError, UserValidationTypeError)
  - User Repository (UserRepositoryError, UserRepositoryTypeError)

The __all__ attribute explicitly defines the names that will be exported when importing
this package.
"""

from .email_error import EmailError, EmailTypeError
from .full_name_error import FullNameError, FullNameTypeError
from .password_error import PasswordError, PasswordTypeError
from .phone_error import PhoneError, PhoneTypeError
from .user_repository_error import UserRepositoryError, UserRepositoryTypeError
from .user_validation_error import UserValidationError, UserValidationTypeError

__all__ = [
    "EmailError",
    "EmailTypeError",
    "FullNameError",
    "FullNameTypeError",
    "PasswordError",
    "PasswordTypeError",
    "UserValidationError",
    "UserValidationTypeError",
    "PhoneError",
    "PhoneTypeError",
    "UserRepositoryError",
    "UserRepositoryTypeError",
]
