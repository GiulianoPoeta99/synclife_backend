from src.api.v1.inventory.application.view_item.view_item_dto import ViewItemDTO
from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.domain.validators.inventory_repository_validator import (
    InventoryRepositoryValidator,
)
from src.api.v1.shared.domain.repositories.session_repository import SessionRepository
from src.api.v1.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class ViewItemUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        session_repository: SessionRepository,
    ):
        self.__inventory_repository = inventory_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewItemDTO) -> Inventory:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        # Valida que el inventario existe
        inventory_item = InventoryRepositoryValidator.inventory_found(
            self.__inventory_repository.find_by_id(Uuid(dto.inventory_id))
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), inventory_item.user_id
        )

        return inventory_item
