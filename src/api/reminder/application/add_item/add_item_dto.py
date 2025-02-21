from dataclasses import dataclass
from datetime import datetime


@dataclass
class AddReminderItemDto:
    user_id: str
    title: str
    content: str
    remind_date: datetime
