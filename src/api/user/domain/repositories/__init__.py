"""
Initialization module for the user domain repositories package.

This module imports and exposes the UserRepository interface, which defines the methods
necessary for managing and persisting user entities in the domain.
"""

from .user_repository import UserRepository

__all__ = ["UserRepository"]
