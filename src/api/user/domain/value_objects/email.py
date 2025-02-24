"""
Module for managing and validating email addresses.

This module defines the Email class, which encapsulates an email address and validates
it using a regular expression. If the address does not meet the expected format, an
EmailError exception is raised with the corresponding error type.
"""

import re

from src.api.user.domain.errors import EmailError, EmailTypeError


class Email:
    """
    Class representing an email address.

    This class allows storing and validating an email address. The validation is
    performed using a regular expression defined in the setter for the email property.
    If the address does not meet the expected format, an EmailError exception is raised.

    Attributes:
        __email (str): Stores the validated email address.
    """

    __email: str

    def __init__(self, email: str) -> None:
        """
        Initializes a new instance of Email and assigns the email address.

        The assignment is performed using the setter, which implies validation of the
        address.

        Args:
            email (str): Email address to assign.

        Raises:
            EmailError: If the provided email does not meet the valid format.
        """
        self.email = email

    def __repr__(self) -> str:
        """
        Returns an unambiguous representation of the Email object.

        Returns:
            str: String representing the object in the format "<Email(email)>".
        """
        return f"<Email({self.email})>"

    def __eq__(self, other: object) -> bool:
        """
        Compares this Email object with another to determine if they are equal.

        The comparison is based on the equality of the email addresses.

        Args:
            other (object): Another object to compare.

        Returns:
            bool: True if 'other' is an instance of Email and both email addresses are
                  equal, False otherwise.
        """
        return self.email == other.email if isinstance(other, Email) else False

    def __str__(self) -> str:
        """
        Returns a readable representation of the Email object.

        Returns:
            str: The stored email address.
        """
        return self.email

    @property
    def email(self) -> str:
        """
        Retrieves the validated email address.

        Returns:
            str: The email address.
        """
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """
        Sets and validates the email address.

        Uses a regular expression to verify that the email has the correct format.
        If the provided value matches the pattern, it is assigned to the property;
        otherwise, an EmailError exception is raised.

        Args:
            value (str): The email address to assign.

        Raises:
            EmailError: If the provided email does not meet the valid format.
        """
        email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"  # noqa: E501
        if re.match(email_regex, value):
            self.__email = value
            return
        raise EmailError(EmailTypeError.INVALID_EMAIL)
