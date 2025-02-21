from src.api.inventory.application.update_item.update_item_dto import UpdateItemDto
from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.errors import InventoryItemError, InventoryItemTypeError
from src.api.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.inventory.domain.validators.inventory_repository_validator import (
    InventoryRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class UpdateItemUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        session_repository: SessionRepository,
    ) -> None:
        self.__inventory_repository = inventory_repository
        self.__session_repository = session_repository

    # Valida que el inventario existe
    def execute(self, dto: UpdateItemDto) -> Inventory:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        inventory_item = InventoryRepositoryValidator.inventory_found(
            self.__inventory_repository.find_by_id(Uuid(dto.inventory_id))
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), inventory_item.user_id
        )

        # Actualiza item
        inventory_item.product_name = str(dto.product_name)
        inventory_item.amount = int(dto.amount)
        inventory_item.expiration_date = dto.expiration_date

        is_updated, updated_item = self.__inventory_repository.update(inventory_item)

        if not is_updated or updated_item is None:
            raise InventoryItemError(InventoryItemTypeError.OPERATION_FAILED)

        return updated_item
