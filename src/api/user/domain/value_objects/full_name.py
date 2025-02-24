"""
Module for managing and validating full names.

This module defines the FullName class, which encapsulates a first name and a last name,
validating their format using a regular expression. If the format is invalid,
a FullNameError exception is raised with the corresponding error type.
"""

import re

from src.api.user.domain.errors import FullNameError, FullNameTypeError


class FullName:
    """
    Class representing a full name.

    This class stores a first name and a last name, validating that they meet the
    proper format. If the first name or last name is invalid, a FullNameError exception
    is raised.

    Attributes:
        __first_name (str): Stores the validated first name.
        __last_name (str): Stores the validated last name.
    """

    __first_name: str
    __last_name: str

    def __init__(self, first_name: str, last_name: str) -> None:
        """
        Initializes a new instance of FullName with a first name and a last name.

        Args:
            first_name (str): First name to assign.
            last_name (str): Last name to assign.

        Raises:
            FullNameError: If the first name or last name do not meet the valid format.
        """
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """
        Returns an unambiguous representation of the FullName object.

        Returns:
            str: String representing the object in the format
                 "<FullName(FirstName LastName)>".
        """
        return f"<FullName({self.first_name} {self.last_name})>"

    def __eq__(self, other: object) -> bool:
        """
        Compares this FullName object with another to determine if they are equal.

        The comparison is based on the equality of the first name and the last name.

        Args:
            other (object): Another object to compare.

        Returns:
            bool: True if 'other' is an instance of FullName and both names match,
                  False otherwise.
        """
        return (
            (self.first_name == other.first_name and self.last_name == other.last_name)
            if isinstance(other, FullName)
            else False
        )

    def __str__(self) -> str:
        """
        Returns a readable representation of the FullName object.

        Returns:
            str: The full name in the format "FirstName LastName".
        """
        return self.get_full_name()

    def get_full_name(self, last_first: bool = False) -> str:
        """
        Retrieves the full name in different formats.

        Args:
            last_first (bool, optional): If True, returns "LastName, FirstName";
                                         otherwise, "FirstName LastName".
                                         Default is False.

        Returns:
            str: The full name in the specified format.
        """
        return (
            f"{self.last_name}, {self.first_name}"
            if last_first
            else f"{self.first_name} {self.last_name}"
        )

    def __validate_format(self, name: str) -> None:
        """
        Validates the format of a first name or last name.

        Checks that the name contains only letters and certain special characters
        (such as hyphens and apostrophes). It also ensures that the length does not
        exceed the allowed limit.

        Args:
            name (str): The first name or last name to validate.

        Raises:
            FullNameError: If the name format is invalid or if it exceeds the maximum
                           allowed length.
        """
        name_regex = r"^[a-zA-Z]+(?:[-' ][a-zA-Z]+)*$"
        if not re.match(name_regex, name):
            raise FullNameError(FullNameTypeError.INVALID_NAME_FORMAT)

        max_name_length = 50
        if len(name) > max_name_length:
            raise FullNameError(FullNameTypeError.NAME_TOO_LONG)

    @property
    def first_name(self) -> str:
        """
        Retrieves the validated first name.

        Returns:
            str: The first name.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, valor: str) -> None:
        """
        Sets and validates the first name.

        Args:
            valor (str): The first name to assign.

        Raises:
            FullNameError: If the first name format is invalid.
        """
        self.__validate_format(valor)
        self.__first_name = valor.title()

    @property
    def last_name(self) -> str:
        """
        Retrieves the validated last name.

        Returns:
            str: The last name.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Sets and validates the last name.

        Args:
            value (str): The last name to assign.

        Raises:
            FullNameError: If the last name format is invalid.
        """
        self.__validate_format(value)
        self.__last_name = value.title()
