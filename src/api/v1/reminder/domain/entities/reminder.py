from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.api.v1.reminder.domain.validators.reminder_validator import ReminderValidator
from src.api.v1.shared.domain.value_objects import Uuid


@dataclass
class Reminder:
    id: Uuid
    user_id: Uuid
    title: str
    content: str
    remind_date: datetime
    updated_at: Optional[datetime]
    is_deleted: bool

    def __post_init__(self) -> None:
        ReminderValidator.validate_all(
            title=self.title,
        )

    def __repr__(self) -> str:
        return (
            f"<Reminder(ID={self.id}, title={self.title}, "
            f"content={self.content},"
            f"remind_date={self.remind_date})>"
        )

    def __str__(self) -> str:
        return (
            f"Title({self.title}, "
            f"Content: {self.content}, ID: {self.id}, "
            f"Remind Date: {self.remind_date}"
        )
