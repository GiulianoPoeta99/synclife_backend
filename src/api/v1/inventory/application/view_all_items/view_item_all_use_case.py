from typing import List

from src.api.v1.inventory.application.view_all_items.view_all_item_dto import (
    ViewAllInventoryItemsDTO,
)
from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.shared.domain.repositories import SessionRepository
from src.api.v1.shared.domain.validators import SessionRepositoryValidator
from src.api.v1.shared.domain.value_objects import Uuid


class ViewAllInventoryItemsUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        session_repository: SessionRepository,
    ):
        self.__inventory_repository = inventory_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAllInventoryItemsDTO) -> List[Inventory]:

        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        inventory_items = self.__inventory_repository.find_all_by_user_id(
            Uuid(user_request_uuid)
        )

        return inventory_items
