from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.api.shared.domain.value_objects import Uuid


@dataclass()
class Tags:
    id: Uuid
    user_id: Uuid
    name: str
    is_deleted: bool
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None

    def __post_init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"<name=({self.name})>"

    def __str__(self) -> str:
        return f"Tag(Tag name: {self.name})"
