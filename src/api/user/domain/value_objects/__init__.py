"""
Initialization module for the user 'value objects' package.

This module imports and exposes the classes:
    - Email: Management and validation of email addresses.
    - FullName: Management and validation of full names.
    - Password: Management, validation, and encryption of passwords.
    - Phone: Validation of phone numbers.

The __all__ attribute is used to explicitly define the names that will be
exported when the package is imported via 'from <package> import *'.
"""

from .email import Email
from .full_name import FullName
from .password import Password
from .phone import Phone

__all__ = ["Email", "FullName", "Password", "Phone"]
