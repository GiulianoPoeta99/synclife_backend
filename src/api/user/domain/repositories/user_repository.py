"""
Module that defines the interface for user repositories.

This module contains the abstract class UserRepository, which specifies the methods
necessary for the persistence and management of user entities.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.shared.domain.value_objects import Uuid
from src.api.user.domain.entities import User
from src.api.user.domain.value_objects import Email


class UserRepository(ABC):
    """
    Interface for user repositories.

    This abstract class defines the methods necessary for managing the
    persistence of user entities, including operations to find,
    save, delete, and update users.
    """

    @abstractmethod
    def find_all(self) -> List[User]:
        """
        Retrieves all users from the repository.

        Returns:
            List[User]: A list of all stored users.
        """
        pass

    @abstractmethod
    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[User]:
        """
        Finds a user by their unique identifier.

        Args:
            id (Uuid): The unique identifier of the user to find.
            include_deleted (bool, optional): Indicates whether to include users
                                              marked as deleted.
                                              Defaults to False.

        Returns:
            Optional[User]: The found user or None if not found.
        """
        pass

    @abstractmethod
    def find_by_email(
        self, email: Email, include_deleted: bool = False, validate: bool = True
    ) -> Optional[User]:
        """
        Finds a user by their email address.

        Args:
            email (Email): The email address of the user to find.
            include_deleted (bool, optional): Indicates whether to include users
                                              marked as deleted.
                                              Defaults to False.
            validate (bool, optional): Indicates whether the email should be validated
                                       before the search.
                                       Defaults to True.

        Returns:
            Optional[User]: The found user or None if not found.
        """
        pass

    @abstractmethod
    def save(self, user: User) -> bool:
        """
        Saves a user in the repository.

        Args:
            user (User): The user to save.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        pass

    @abstractmethod
    def delete(self, user: User) -> Tuple[bool, Optional[User]]:
        """
        Deletes a user from the repository.

        Args:
            user (User): The user to delete.

        Returns:
            Tuple[bool, Optional[User]]: A tuple where the first value indicates whether
                                         the deletion was successful and the second 
                                         value is the deleted user (or None if not found
                                         or not deleted).
        """
        pass

    @abstractmethod
    def update(self, user: User) -> Tuple[bool, Optional[User]]:
        """
        Updates the information of a user in the repository.

        Args:
            user (User): The user with updated information.

        Returns:
            Tuple[bool, Optional[User]]: A tuple where the first value indicates whether
                                         the update was successful and the second value
                                         is the updated user (or None if the update
                                         could not be performed).
        """
        pass
