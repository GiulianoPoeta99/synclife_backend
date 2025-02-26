"""
Module that defines the DTO for the account view use case in the user application.

This DTO encapsulates the necessary information to request the viewing of a user's
account, using the session token to validate the authenticity of the request.
"""

from dataclasses import dataclass


@dataclass
class ViewAccountDTO:
    """
    Data Transfer Object for the use case of viewing a user's account.

    Attributes:
        session_token (str): User's session token, used to validate the request and
                             access the account.
    """

    session_token: str
