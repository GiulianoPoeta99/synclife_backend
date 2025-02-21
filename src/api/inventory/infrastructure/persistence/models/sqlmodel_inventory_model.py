from datetime import date
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.api.inventory.domain.entities.inventory import Inventory
from src.api.shared.domain.value_objects import Uuid
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class SqlModelInventoryModel(SQLModel, table=True):
    __tablename__ = "inventory_item"

    id: str = Field(primary_key=True)
    user_id: str = Field(foreign_key="users.id")
    product_name: str
    amount: int
    expiration_date: date
    is_deleted: bool = Field(default=False)
    created_at: date = Field(default_factory=date.today)
    updated_at: Optional[date] = Field(default=None)
    user: "SqlModelUserModel" = Relationship(back_populates="inventory_items")

    @classmethod
    def from_entity(cls, entity: "Inventory") -> "SqlModelInventoryModel":

        return cls(
            id=str(entity.id),
            user_id=str(entity.user_id),
            product_name=str(entity.product_name),
            amount=int(entity.amount),
            expiration_date=str(entity.expiration_date),
            is_deleted=False,
        )

    def to_entity(self) -> "Inventory":
        return Inventory(
            id=Uuid(self.id),
            user_id=Uuid(self.user_id),
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
        )
