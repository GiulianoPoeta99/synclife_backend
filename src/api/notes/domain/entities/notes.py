from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from src.api.notes.domain.entities.tags import Tags
from src.api.notes.domain.validators.notes import NotesValidator
from src.api.shared.domain.value_objects import Uuid


@dataclass()
class Notes:
    id: Uuid
    user_id: Uuid
    title: str
    content: str
    is_deleted: bool
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
    tags: List[Tags] = field(default_factory=list)

    def __post_init__(self) -> None:
        NotesValidator.validate_all(
            title=self.title,
            content=self.content,
        )

    def add_tag(self, tag: Tags) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: Tags) -> None:
        if tag in self.tags:
            self.tags.remove(tag)

    def __repr__(self) -> str:
        return (
            f"<title(={self.title},"
            f"content={self.content},"
            f"created_at={self.created_at})>"
        )

    def __str__(self) -> str:
        return (
            f"Note(Note title: {self.title},"
            f"Content: {self.content},"
            f"Created at: {self.created_at})"
        )
