"""
Module that defines the User entity.

This module contains the User class, which represents the user entity in the
application domain. It encapsulates attributes such as uuid, email, password,
full_name, birth_date, phone, is_deleted, created_at, and updated_at. Additionally,
specific validations are performed; for example, in the birth_date setter it is verified
that the user is at least 16 years old and that the date is not later than the current
date.
"""

from datetime import date, datetime
from typing import Optional

from src.api.shared.domain.value_objects import Uuid
from src.api.user.domain.errors import UserValidationError, UserValidationTypeError
from src.api.user.domain.value_objects import Email, FullName, Password
from src.api.user.domain.value_objects.phone import Phone


class User:
    """
    Class representing the user entity.

    This class encapsulates all relevant data for a user, such as:
      - uuid: Unique identifier of the user.
      - email: Email address.
      - password: User's password.
      - full_name: Full name.
      - birth_date: Date of birth.
      - phone: Phone number.
      - is_deleted: Deletion status.
      - created_at: Date and time of creation.
      - updated_at: Date and time of last update (optional).

    Attributes:
        __uuid (Uuid): Unique identifier of the user.
        __email (Email): Email address.
        __password (Password): User's encrypted password.
        __full_name (FullName): User's full name.
        __birth_date (date): User's date of birth.
        __phone (Phone): User's phone number.
        __is_deleted (bool): Indicates whether the user has been marked as deleted.
        __created_at (datetime): User's creation date and time.
        __updated_at (Optional[datetime]): Date and time of the last update.
    """

    __uuid: Uuid
    __email: Email
    __password: Password
    __full_name: FullName
    __birth_date: date
    __phone: Phone
    __is_deleted: bool
    __created_at: datetime
    __updated_at: Optional[datetime]

    def __init__(
        self,
        uuid: Uuid,
        email: Email,
        password: Password,
        full_name: FullName,
        birth_date: date,
        phone: Phone,
        is_deleted: bool,
        created_at: datetime,
        updated_at: Optional[datetime],
    ) -> None:
        """
        Initializes a new instance of User.

        Assigns all user attributes using their respective setters, which allows for
        validation of certain fields (for example, the date of birth).

        Args:
            uuid (Uuid): Unique identifier of the user.
            email (Email): Email address.
            password (Password): User's password.
            full_name (FullName): User's full name.
            birth_date (date): User's date of birth.
            phone (Phone): User's phone number.
            is_deleted (bool): Deletion status of the user.
            created_at (datetime): Creation date and time.
            updated_at (Optional[datetime]): Date and time of the last update;
                                             may be None.

        Raises:
            UserValidationError: If the date of birth is not valid (for example, if the
                                 user is less than 16 years old or if the date is later
                                 than the current date).
        """
        self.uuid = uuid
        self.email = email
        self.password = password
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.is_deleted = is_deleted
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        """
        Returns an unambiguous representation of the User object.

        Returns:
            str: A string representing the object in the format
                 "<User(uuid=..., email=..., phone=...)>".
        """
        return f"<User(uuid={self.uuid}, email={self.email}, phone={self.phone})>"

    def __str__(self) -> str:
        """
        Returns a readable representation of the User object.

        Returns:
            str: A string with relevant user information, including full name, email,
                 uuid, date of birth, and phone.
        """
        return (
            f"User({self.full_name.get_full_name()}, "
            f"Email: {self.email}, UUID: {self.uuid}, "
            f"Birth Date: {self.birth_date}, "
            f"Phone: {self.phone})"
        )

    @property
    def uuid(self) -> Uuid:
        """
        Gets the unique identifier of the user.

        Returns:
            Uuid: The unique identifier of the user.
        """
        return self.__uuid

    @uuid.setter
    def uuid(self, valor: Uuid) -> None:
        """
        Sets the unique identifier of the user.

        Args:
            valor (Uuid): The new unique identifier to assign.
        """
        self.__uuid = valor

    @property
    def email(self) -> Email:
        """
        Gets the user's email address.

        Returns:
            Email: The email address.
        """
        return self.__email

    @email.setter
    def email(self, valor: Email) -> None:
        """
        Sets the user's email address.

        Args:
            valor (Email): The new email address to assign.
        """
        self.__email = valor

    @property
    def password(self) -> Password:
        """
        Gets the user's password.

        Returns:
            Password: The user's encrypted password.
        """
        return self.__password

    @password.setter
    def password(self, valor: Password) -> None:
        """
        Sets the user's password.

        Args:
            valor (Password): The new password to assign.
        """
        self.__password = valor

    @property
    def full_name(self) -> FullName:
        """
        Gets the user's full name.

        Returns:
            FullName: The user's full name.
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, valor: FullName) -> None:
        """
        Sets the user's full name.

        Args:
            valor (FullName): The new full name to assign.
        """
        self.__full_name = valor

    @property
    def birth_date(self) -> date:
        """
        Gets the user's date of birth.

        Returns:
            date: The user's date of birth.
        """
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, valor: date) -> None:
        """
        Sets the user's date of birth and validates that it is correct.

        It validates that the date is not later than the current date and that the user
        is at least 16 years old.

        Args:
            valor (date): The date of birth to assign.

        Raises:
            UserValidationError: If the user is less than 16 years old or if the date is
                                 later than the current date.
        """
        today = date.today()
        minimum_age = 16
        age = (
            today.year
            - valor.year
            - ((today.month, today.day) < (valor.month, valor.day))
        )

        if (age < minimum_age) or (valor > today):
            raise UserValidationError(UserValidationTypeError.INVALID_BIRTHDATE)
        self.__birth_date = valor

    @property
    def phone(self) -> Phone:
        """
        Gets the user's phone number.

        Returns:
            Phone: The phone number.
        """
        return self.__phone

    @phone.setter
    def phone(self, valor: Phone) -> None:
        """
        Sets the user's phone number.

        Args:
            valor (Phone): The new phone number to assign.
        """
        self.__phone = valor

    @property
    def is_deleted(self) -> bool:
        """
        Gets the user's deletion status.

        Returns:
            bool: True if the user has been marked as deleted, False otherwise.
        """
        return self.__is_deleted

    @is_deleted.setter
    def is_deleted(self, valor: bool) -> None:
        """
        Sets the user's deletion status.

        Args:
            valor (bool): Deletion status to assign (True if deleted, False otherwise).
        """
        self.__is_deleted = valor

    @property
    def created_at(self) -> datetime:
        """
        Gets the user's creation date and time.

        Returns:
            datetime: The creation date and time.
        """
        return self.__created_at

    @created_at.setter
    def created_at(self, valor: datetime) -> None:
        """
        Sets the user's creation date and time.

        Args:
            valor (datetime): The creation date and time to assign.
        """
        self.__created_at = valor

    @property
    def updated_at(self) -> Optional[datetime]:
        """
        Gets the user's last update date and time.

        Returns:
            Optional[datetime]: The date and time of the last update, or None if it
                                hasn't been updated.
        """
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, valor: Optional[datetime]) -> None:
        """
        Sets the user's last update date and time.

        Args:
            valor (Optional[datetime]): The last update date and time to assign.
        """
        self.__updated_at = valor
