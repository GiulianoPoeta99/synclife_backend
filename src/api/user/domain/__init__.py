"""
User Domain Initialization Module.

This module centralizes the import and exposure of the entities, errors,
repositories, validators, and value objects related to the user domain. By
defining the __all__ attribute, the elements that will be exported when the package is
imported using 'from <package> import *' are explicitly specified.
"""

from .entities import User
from .errors import (
    EmailError,
    EmailTypeError,
    FullNameError,
    FullNameTypeError,
    PasswordError,
    PasswordTypeError,
    PhoneError,
    PhoneTypeError,
    UserRepositoryError,
    UserRepositoryTypeError,
    UserValidationError,
    UserValidationTypeError,
)
from .repositories import UserRepository
from .validators import UserRepositoryValidator
from .value_objects import Email, FullName, Password, Phone

__all__ = [
    "User",
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
    "UserRepository",
    "UserRepositoryValidator",
    "Email",
    "FullName",
    "Password",
    "Phone",
]
