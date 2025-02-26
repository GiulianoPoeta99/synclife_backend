"""
Module that defines the DTO for the login use case in the user application layer.

This module contains the LoginDTO class, which is used to transport the necessary data
for the authentication process by encapsulating the user's email address and password.
"""

from dataclasses import dataclass


@dataclass
class LoginDTO:
    """
    Data Transfer Object for the login use case.

    This class encapsulates the data required for a user's authentication process,
    including:
      - email: The user's email address.
      - password: The user's password.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
    """

    email: str
    password: str
