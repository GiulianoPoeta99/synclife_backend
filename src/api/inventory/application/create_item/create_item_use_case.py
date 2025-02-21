from src.api.inventory.application.create_item.create_item_dto import CreateItemDto
from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class CreateItemUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        user_repository: UserRepository,
        session_repository: SessionRepository,
    ):
        self.__inventory_repository = inventory_repository
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: CreateItemDto) -> Inventory:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        user_request_uuid = Uuid(user_request_uuid)

        # Valida si el usuario existe
        UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(user_request_uuid)
        )

        # Crear y guardar el inventario
        inventory_item = Inventory(
            id=Uuid(),
            user_id=user_request_uuid,
            product_name=str(dto.product_name),
            amount=int(dto.amount),
            expiration_date=dto.expiration_date,
        )
        self.__inventory_repository.save(inventory_item)
        return inventory_item
