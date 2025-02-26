"""
Initialization module for the functionality of modifying personal information in the
user application.

This module imports and exposes the necessary components to update the user's personal
information:
  - ChangePersonalInformationDTO: DTO that encapsulates the new personal data.
  - ChangePersonalInformationUseCase: Use case that implements the logic for modifying
    personal information.

The __all__ attribute explicitly defines the names that will be exported when importing
this package.
"""

from .change_personal_information_dto import ChangePersonalInformationDTO
from .change_personal_information_use_case import ChangePersonalInformationUseCase

__all__ = ["ChangePersonalInformationDTO", "ChangePersonalInformationUseCase"]
