"""
Module for managing and validating passwords.

This module defines the Password class, which allows you to store a password securely
through encryption.
Various aspects of the password format are validated (length, presence of digits,
uppercase letters, lowercase letters, special characters, and strength evaluated by
zxcvbn). If the password does not meet the criteria, a PasswordError exception is raised
with the corresponding error type.
"""

import re

import bcrypt
from zxcvbn import zxcvbn

from src.api.user.domain.errors import PasswordError, PasswordTypeError


class Password:
    """
    Class representing and managing a password.

    This class allows you to store and validate passwords. Additionally, it encrypts the
    password using bcrypt. You can choose whether to validate the password format during
    assignment via the 'validate' parameter.

    Attributes:
        __password (str): Encrypted password.
        __validate (bool): Indicates whether the password format should be validated
                           upon assignment.
    """

    __password: str
    __validate: bool = True

    def __init__(self, password: str, validate: bool = True) -> None:
        """
        Initializes a new instance of Password.

        Assigns the password, applying validation and encryption as needed.

        Args:
            password (str): The plaintext password to assign.
            validate (bool, optional): Determines whether the password format should be
                                       validated.
                                       Defaults to True.

        Raises:
            PasswordError: If the plaintext password does not meet the validation
                           criteria.
        """
        self.__validate = validate
        self.password = password

    def __repr__(self) -> str:
        """
        Returns an unambiguous representation of the Password object.

        Returns:
            str: Representation of the object in the format "<Password(***)>".
        """
        return "<Password(***)>"

    def __eq__(self, other: object) -> bool:
        """
        Compares this Password object with another to determine if they are equal.

        The comparison is based on the equality of the encrypted passwords.

        Args:
            other (object): Another object to compare.

        Returns:
            bool: True if 'other' is an instance of Password and the passwords are
                  equal, False otherwise.
        """
        return self.password == other.password if isinstance(other, Password) else False

    def __str__(self) -> str:
        """
        Returns a readable, masked representation of the password.

        Returns:
            str: A string that hides the actual content of the password ("********").
        """
        return "********"

    def check_password(self, plain_password: str) -> bool:
        """
        Verifies if the plaintext password matches the stored encrypted password.

        Uses bcrypt to compare the plaintext password with the encrypted password.

        Args:
            plain_password (str): The plaintext password to verify.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        return bcrypt.checkpw(plain_password.encode(), self.password.encode())

    def __is_encrypted(self, password: str) -> bool:
        """
        Determines if a password is already encrypted.

        Checks that the password starts with "$2b$" and has a length of 60 characters,
        which is the expected bcrypt format.

        Args:
            password (str): The password to evaluate.

        Returns:
            bool: True if the password appears to be encrypted, False otherwise.
        """
        return password.startswith("$2b$") and len(password) == 60

    def __validate_format(self, password: str) -> None:
        """
        Validates the format of a plaintext password.

        The following validations are performed:
          - Minimum length of 8 characters.
          - At least one digit.
          - At least one uppercase letter.
          - At least one lowercase letter.
          - At least one special character.
          - The strength of the password is evaluated with zxcvbn and must have a score
            of at least 3.

        Args:
            password (str): The plaintext password to validate.

        Raises:
            PasswordError: If the password does not meet one or more of the validation
                           criteria.
        """
        if len(password) < 8:
            raise PasswordError(PasswordTypeError.TOO_SHORT)
        if not re.search(r"\d", password):
            raise PasswordError(PasswordTypeError.MISSING_NUMBER)
        if not re.search(r"[A-Z]", password):
            raise PasswordError(PasswordTypeError.MISSING_UPPERCASE)
        if not re.search(r"[a-z]", password):
            raise PasswordError(PasswordTypeError.MISSING_LOWERCASE)
        if not re.search(r"[\W_]", password):
            raise PasswordError(PasswordTypeError.MISSING_SPECIAL)

        result = zxcvbn(password)
        if result["score"] < 3:
            raise PasswordError(PasswordTypeError.WEAK_PASSWORD)

    def __encrypt_password(self, password: str) -> str:
        """
        Encrypts a password using bcrypt.

        Args:
            password (str): The plaintext password to encrypt.

        Returns:
            str: The encrypted password.
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @property
    def password(self) -> str:
        """
        Retrieves the encrypted password.

        Returns:
            str: The stored encrypted password.
        """
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        """
        Sets the password, applying validation and encryption if necessary.

        If the password is not already encrypted, its format is validated (if
        validation is enabled) and then encrypted. Otherwise, it is assigned directly.

        Args:
            value (str): The plaintext or encrypted password to assign.

        Raises:
            PasswordError: If the plaintext password does not meet the validation
                           criteria.
        """
        if not self.__is_encrypted(value):
            if self.__validate:
                self.__validate_format(value)
            self.__password = self.__encrypt_password(value)
        else:
            self.__password = value
