from dataclasses import dataclass
from datetime import datetime


@dataclass
class ModifyReminderItemDto:
    reminder_id: str
    title: str
    content: str
    user_id: str
    remind_date: datetime
