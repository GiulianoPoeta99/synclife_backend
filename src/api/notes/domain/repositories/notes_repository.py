from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.notes.domain.entities.notes import Notes
from src.api.shared.domain.value_objects import Uuid


class NotesRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Notes]:
        pass

    @abstractmethod
    def find_by_id(self, id: Uuid) -> Optional[Notes]:
        pass

    @abstractmethod
    def find_by_tag(self, tag_id: Uuid) -> List[Notes]:
        pass

    @abstractmethod
    def find_all_by_user_id(
        self, id: Uuid, include_deleted: bool = False
    ) -> List[Notes]:
        pass

    @abstractmethod
    def find_by_title_and_user_id(self, title: str, user_id: Uuid) -> Optional[Notes]:
        pass

    @abstractmethod
    def save(self, note: Notes) -> bool:
        pass

    @abstractmethod
    def delete(self, note: Notes) -> Tuple[bool, Optional[Notes]]:
        pass

    @abstractmethod
    def update(self, note: Notes) -> Tuple[bool, Optional[Notes]]:
        pass
