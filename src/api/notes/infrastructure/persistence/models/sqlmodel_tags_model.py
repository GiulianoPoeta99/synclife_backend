from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.api.notes.domain.entities.tags import Tags
from src.api.notes.infrastructure.persistence.models.sqlmodel_note_tag_link_model import (  # noqa: E501
    NotesTagsLink,
)
from src.api.shared.domain.value_objects import Uuid

if TYPE_CHECKING:
    from src.api.notes.infrastructure.persistence.models.sqlmodel_notes_model import (  # noqa: E501
        SqlModelNotesModel,
    )
    from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
        SqlModelUserModel,
    )


class SqlModelTagsModel(SQLModel, table=True):
    __tablename__ = "tags"

    id: str = Field(primary_key=True)
    user_id: str = Field(foreign_key="users.id")
    name: str
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.today)
    updated_at: Optional[datetime] = Field(default=None)
    user: "SqlModelUserModel" = Relationship(back_populates="tags")
    notes: List["SqlModelNotesModel"] = Relationship(
        back_populates="tags", link_model=NotesTagsLink
    )

    @classmethod
    def from_entity(cls, entity: "Tags") -> "SqlModelTagsModel":
        return cls(
            id=str(entity.id),
            user_id=str(entity.user_id),
            name=entity.name.strip(),
            is_deleted=False,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> "Tags":
        return Tags(
            id=Uuid(self.id),
            user_id=Uuid(self.user_id),
            name=self.name,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
