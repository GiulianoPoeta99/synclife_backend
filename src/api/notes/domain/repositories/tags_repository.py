from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.notes.domain.entities.tags import Tags
from src.api.shared.domain.value_objects import Uuid


class TagsRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Tags]:
        pass

    @abstractmethod
    def find_by_id(self, id: Uuid) -> Optional[Tags]:
        pass

    @abstractmethod
    def find_all_by_user_id(
        self, id: Uuid, include_deleted: bool = False
    ) -> List[Tags]:
        pass

    @abstractmethod
    def find_by_name_and_user_id(self, name: str, user_id: Uuid) -> Optional[Tags]:
        pass

    @abstractmethod
    def save(self, tag: Tags) -> bool:
        pass

    @abstractmethod
    def delete(self, tag: Tags) -> Tuple[bool, Optional[Tags]]:
        pass

    @abstractmethod
    def update(self, tag: Tags) -> Tuple[bool, Optional[Tags]]:
        pass
