from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class SqlModelReminderModel(SQLModel, table=True):
    __tablename__ = "reminder"  # Nota: usa "__tablename__"

    id: str = Field(primary_key=True, nullable=False, max_length=36)  # UUID como string
    user_id: str = Field(foreign_key="users.id", nullable=False, max_length=36)
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    remind_date: datetime = Field(nullable=False)
    is_deleted: bool = Field(default=False, nullable=False)
    updated_at: Optional[datetime] = Field(default=None)
    user: "SqlModelUserModel" = Relationship(back_populates="reminder_items")

    @classmethod
    def from_entity(cls, entity: "Reminder") -> "SqlModelReminderModel":
        return cls(
            id=str(entity.id),
            user_id=str(entity.user_id),
            title=entity.title,
            content=entity.content,
            remind_date=entity.remind_date,
            updated_at=entity.updated_at,
            created_at=entity.created_at,
            is_deleted=entity.is_deleted,
        )

    def to_entity(self) -> "Reminder":
        return Reminder(
            id=Uuid(self.id),
            user_id=Uuid(self.user_id),
            title=self.title,
            content=self.content,
            remind_date=self.remind_date,
            updated_at=self.updated_at,
            created_at=self.created_at,
            is_deleted=self.is_deleted,
        )
