"""
Module for managing and validating phone numbers.

This module defines the Phone class, which encapsulates a phone number and validates it
using a regular expression. If the number does not meet the expected format, a
PhoneError exception is raised.
"""

import re

from src.api.user.domain.errors import PhoneError, PhoneTypeError


class Phone:
    """
    Class representing a phone number.

    This class stores and validates a phone number. The validation is performed
    using a regular expression in the phone property's setter. If the number does not
    meet the specified format, a PhoneError exception is raised.

    Attributes:
        __phone (str): Stores the validated phone number.
    """

    __phone: str

    def __init__(self, phone: str) -> None:
        """
        Initializes a new instance of Phone with a phone number.

        The number is assigned using the setter, which implies its validation.

        Args:
            phone (str): Phone number to assign.

        Raises:
            PhoneError: If the phone number does not meet the valid format.
        """
        self.phone = phone

    def __repr__(self) -> str:
        """
        Returns an unambiguous representation of the Phone object.

        Returns:
            str: String representing the object in the format "<Phone(number)>".
        """
        return f"<Phone({self.phone})>"

    def __str__(self) -> str:
        """
        Returns a readable representation of the phone number.

        Returns:
            str: The stored phone number.
        """
        return self.phone

    def __eq__(self, other: object) -> bool:
        """
        Compares this Phone object with another to determine if they are equal.

        The comparison is based on the equality of the phone number.

        Args:
            other (object): Another object to compare.

        Returns:
            bool: True if 'other' is an instance of Phone and the phone numbers
                  are equal, False otherwise.
        """
        return self.phone == other.phone if isinstance(other, Phone) else False

    @property
    def phone(self) -> str:
        """
        Retrieves the validated phone number.

        Returns:
            str: The phone number.
        """
        return self.__phone

    @phone.setter
    def phone(self, value: str) -> None:
        """
        Sets and validates the phone number.

        Uses a regular expression to verify that the number has a correct format.
        If the provided value does not match the pattern, a PhoneError exception
        is raised.

        Args:
            value (str): Phone number to assign.

        Raises:
            PhoneError: If the phone number does not meet the valid format.
        """
        phone_regex = r"^\+?1?\d{9,15}$"
        if not re.match(phone_regex, value):
            raise PhoneError(PhoneTypeError.INVALID_PHONE)
        self.__phone = value
