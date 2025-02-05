from dataclasses import dataclass

from src.api.v1.shared.domain.value_objects import Uuid


@dataclass
class ViewAllReminderItemsDto:
    user_id: Uuid
