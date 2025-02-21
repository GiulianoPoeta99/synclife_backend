from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.api.notes.domain.entities.notes import Notes
from src.api.notes.infrastructure.persistence.models.sqlmodel_note_tag_link_model import (  # noqa: E501
    NotesTagsLink,
)
from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SqlModelTagsModel,
)
from src.api.shared.domain.value_objects import Uuid
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class SqlModelNotesModel(SQLModel, table=True):
    __tablename__ = "notes"

    id: str = Field(primary_key=True)
    user_id: str = Field(foreign_key="users.id")
    title: str
    content: str
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.today)
    updated_at: Optional[datetime] = Field(default=None)
    user: "SqlModelUserModel" = Relationship(back_populates="notes")
    tags: List["SqlModelTagsModel"] = Relationship(
        back_populates="notes", link_model=NotesTagsLink
    )

    @classmethod
    def from_entity(cls, entity: "Notes") -> "SqlModelNotesModel":
        return cls(
            id=str(entity.id),
            user_id=str(entity.user_id),
            title=entity.title.strip(),
            content=entity.content.strip(),
            is_deleted=False,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> "Notes":
        return Notes(
            id=Uuid(self.id),
            user_id=Uuid(self.user_id),
            title=self.title,
            content=self.content,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
