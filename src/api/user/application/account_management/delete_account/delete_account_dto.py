"""
Module that defines the DTO for the account deletion use case in the user application
layer.

This DTO encapsulates the necessary information to request a user's account deletion,
specifically the session token, which is used to validate the authenticity of the
request.
"""

from dataclasses import dataclass


@dataclass
class DeleteAccountDTO:
    """
    Data Transfer Object for the user account deletion use case.

    Attributes:
        session_token (str): The user's session token, used to validate the deletion
                             request.
    """

    session_token: str
