from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.inventory.domain.entities.inventory import Inventory
from src.api.shared.domain.value_objects import Uuid


class InventoryRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Inventory]:
        pass

    @abstractmethod
    def find_by_id(self, id: Uuid) -> Optional[Inventory]:
        pass

    @abstractmethod
    def find_all_by_user_id(
        self, id: Uuid, include_deleted: bool = False
    ) -> List[Inventory]:
        pass

    @abstractmethod
    def save(self, product: Inventory) -> bool:
        pass

    @abstractmethod
    def delete(self, product: Inventory) -> Tuple[bool, Optional[Inventory]]:
        pass

    @abstractmethod
    def update(self, product: Inventory) -> Tuple[bool, Optional[Inventory]]:
        pass
