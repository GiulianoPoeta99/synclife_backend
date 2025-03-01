from abc import ABC, abstractmethod
from typing import Optional

from src.api.shared.domain.value_objects import Uuid


class VerifyAccountRepository(ABC):
    @abstractmethod
    def create_validation_request(self, user_uuid: Uuid) -> str:
        pass

    @abstractmethod
    def find_user_from_validation_request(self, validate_token: str) -> Optional[Uuid]:
        pass

    @abstractmethod
    def delete_validation_request(self, validation_token: str) -> None:
        pass
