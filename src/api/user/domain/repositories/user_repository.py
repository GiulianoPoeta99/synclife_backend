from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.shared.domain.value_objects import Uuid
from src.api.user.domain.entities import User
from src.api.user.domain.value_objects import Email


class UserRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(
        self, email: Email, include_deleted: bool = False, validate: bool = True
    ) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> bool:
        pass

    @abstractmethod
    def delete(self, user: User) -> Tuple[bool, Optional[User]]:
        pass

    @abstractmethod
    def update(self, user: User) -> Tuple[bool, Optional[User]]:
        pass
