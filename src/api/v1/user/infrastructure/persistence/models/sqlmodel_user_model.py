from datetime import date, datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.orm import Mapped
from sqlmodel import Field, Relationship, SQLModel

from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.value_objects import Email, FullName, Password, Phone

"""
Esto es para la importacion circular, ya que, SQLMODEL importa
el modelo desde un solo lado de la relacion y el otro se hace con
importacion de cadena. Pero pylance y flake8 no deja tener una variable sin definir.
"""

if TYPE_CHECKING:
    from src.api.v1.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
        SqlModelInventoryModel,
    )
    from src.api.v1.notes.infrastructure.persistence.models.sqlmodel_notes_model import (  # noqa: E501
        SqlModelNotesModel,
    )
    from src.api.v1.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
        SqlModelTagsModel,
    )
    from src.api.v1.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (  # noqa: E501
        SqlModelReminderModel,
    )


class SqlModelUserModel(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str
    first_name: str
    last_name: str
    birth_date: date
    phone: str
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)

    # Relaciones con inventory,notes y tags
    inventory_items: Mapped[List["SqlModelInventoryModel"]] = Relationship(
        back_populates="user"
    )
    notes: Mapped[List["SqlModelNotesModel"]] = Relationship(back_populates="user")
    tags: Mapped[List["SqlModelTagsModel"]] = Relationship(back_populates="user")
    reminder_items: Mapped[List["SqlModelReminderModel"]] = Relationship(
        back_populates="user"
    )

    @classmethod
    def from_entity(cls, entity: User) -> "SqlModelUserModel":
        return cls(
            id=str(entity.uuid.id),
            email=entity.email.email,
            password=entity.password.password,
            first_name=entity.full_name.first_name,
            last_name=entity.full_name.last_name,
            birth_date=entity.birth_date,
            phone=entity.phone.phone,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self, validate: bool = True) -> User:
        return User(
            uuid=Uuid(self.id),
            email=Email(self.email),
            password=Password(self.password, validate),
            full_name=FullName(self.first_name, self.last_name),
            birth_date=self.birth_date,
            phone=Phone(self.phone),
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
