from dataclasses import dataclass


@dataclass
class ViewReminderItemDto:
    reminder_id: str
    user_id: str
