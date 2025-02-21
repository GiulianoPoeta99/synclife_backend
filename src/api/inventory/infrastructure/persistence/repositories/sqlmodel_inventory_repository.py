from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SqlModelInventoryModel,
)
from src.api.shared.domain.value_objects import Uuid
from src.api.shared.infrastructure.persistence import get_db_connection


class SQLModelInventoryRepository(InventoryRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SQLModelInventoryRepository":
        with get_db_connection() as db_connection:
            return SQLModelInventoryRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[Inventory]:
        query = (
            select(SqlModelInventoryModel)
            if include_deleted
            else select(SqlModelInventoryModel).where(
                not_(SqlModelInventoryModel.is_deleted)
            )
        )
        items = self.db_connection.exec(query).all()
        return [item.to_entity() for item in items]

    def find_by_id(
        self, id: Uuid, include_deleted: bool = False
    ) -> Optional[Inventory]:
        query = (
            select(SqlModelInventoryModel).where(SqlModelInventoryModel.id == str(id))
            if include_deleted
            else (
                select(SqlModelInventoryModel)
                .where(SqlModelInventoryModel.id == str(id))
                .where(not_(SqlModelInventoryModel.is_deleted))
            )
        )
        item = self.db_connection.exec(query).first()
        return item.to_entity() if item else None

    def find_all_by_user_id(
        self, user_id: Uuid, include_deleted: bool = False
    ) -> List[Inventory]:
        query = select(SqlModelInventoryModel).where(
            SqlModelInventoryModel.user_id == str(user_id)
        )

        if not include_deleted:
            query = query.where(not_(SqlModelInventoryModel.is_deleted))

        items = self.db_connection.exec(query).all()
        return [item.to_entity() for item in items]

    def save(self, item: Inventory) -> bool:
        item_model = SqlModelInventoryModel.from_entity(item)
        self.db_connection.add(item_model)
        self.db_connection.commit()
        return True

    def update(self, item: Inventory) -> Tuple[bool, Optional[Inventory]]:
        existing_item = self.db_connection.exec(
            select(SqlModelInventoryModel)
            .where(SqlModelInventoryModel.id == str(item.id))
            .where(not_(SqlModelInventoryModel.is_deleted))
        ).first()

        if not existing_item:
            return (False, None)

        updates = {
            "product_name": item.product_name,
            "amount": item.amount,
            "expiration_date": item.expiration_date,
            "updated_at": datetime.now(),
        }
        for field, value in updates.items():
            if getattr(existing_item, field) != value:
                setattr(existing_item, field, value)

        self.db_connection.add(existing_item)
        self.db_connection.commit()
        self.db_connection.refresh(existing_item)

        result = (True, existing_item.to_entity())
        print(f"update() result: {result}")  # Imprime el resultado antes de devolverlo
        return result

    def delete(self, item: Inventory) -> Tuple[bool, Optional[Inventory]]:
        existing_item = self.db_connection.exec(
            select(SqlModelInventoryModel)
            .where(SqlModelInventoryModel.id == str(item.id))
            .where(not_(SqlModelInventoryModel.is_deleted))
        ).first()

        if not existing_item:
            return (False, None)

        existing_item.is_deleted = True
        existing_item.updated_at = datetime.now()
        self.db_connection.add(existing_item)
        self.db_connection.commit()
        self.db_connection.refresh(existing_item)

        return (True, existing_item.to_entity())
