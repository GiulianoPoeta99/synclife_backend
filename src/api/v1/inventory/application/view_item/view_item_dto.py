from dataclasses import dataclass


@dataclass
class ViewItemDTO:
    inventory_id: str
    session_token: str
