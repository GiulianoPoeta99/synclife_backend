"""
Module defining the DTO for modifying personal information in the user application
layer.

This DTO encapsulates the necessary data to update a user's personal information,
including email, first name, last name, date of birth, phone number, and the session
token used to validate the request.
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class ChangePersonalInformationDTO:
    """
    Data Transfer Object for the use case of modifying a user's personal information.

    Attributes:
        email (str): User's email address.
        first_name (str): User's first name.
        last_name (str): User's last name.
        birth_date (date): User's date of birth.
        phone (str): User's phone number.
        session_token (str): User's session token, used to validate the modification
                             request.
    """

    email: str
    first_name: str
    last_name: str
    birth_date: date
    phone: str
    session_token: str
