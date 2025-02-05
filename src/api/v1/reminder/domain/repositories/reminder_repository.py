from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.shared.domain.value_objects import Uuid


class ReminderRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Reminder]:
        pass

    @abstractmethod
    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[Reminder]:
        pass

    @abstractmethod
    def find_all_by_user_id(
        self, id: Uuid, include_deleted: bool = False
    ) -> List[Reminder]:
        pass

    @abstractmethod
    def save(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        pass

    @abstractmethod
    def delete(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        pass

    @abstractmethod
    def update(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        pass
