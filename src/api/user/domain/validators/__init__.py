"""
Initialization module for the user domain validators package.

This module imports and exposes the user repository validator, which contains
methods to perform specific validations related to the existence of users and
the availability of emails in the repository.
"""

from .user_repository_validator import UserRepositoryValidator

__all__ = ["UserRepositoryValidator"]
