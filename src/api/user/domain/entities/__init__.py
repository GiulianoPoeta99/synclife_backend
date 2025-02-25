"""
Initialization module for the user entities package.

This module imports and exposes the User class, which represents the primary user entity
in the domain. The __all__ attribute is used to explicitly define the names that will be
exported when the package is imported via 'from <package> import *'.
"""

from .user import User

__all__ = ["User"]
