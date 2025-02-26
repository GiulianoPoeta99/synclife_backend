"""
Module that defines errors in the user domain.

This module contains the UserError class, which is the base exception used to represent
errors related to the user domain. It is expected that the error is passed as a
dictionary that contains a descriptive message and an error code.
"""

from typing import Dict


class UserError(Exception):
    """
    Base exception for errors in the user domain.

    This exception encapsulates an error defined by a dictionary that should contain a
    descriptive message and an identifier code for the error.

    Attributes:
        code (int | str): Error code that identifies the type of error.
    """

    def __init__(self, error: Dict[str, int | str]):
        """
        Initializes the UserError exception.

        Args:
            error (Dict[str, int | str]): Dictionary that contains the key "msg" for
                                          the error message and the key "code" for the
                                          error code.
        """
        super().__init__(error["msg"])
        self.code = error["code"]
