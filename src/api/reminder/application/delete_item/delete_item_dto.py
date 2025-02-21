from dataclasses import dataclass


@dataclass
class DeleteReminderItemDto:
    reminder_id: str
    user_id: str
