from dataclasses import dataclass


@dataclass
class DeleteItemDTO:
    inventory_id: str
    session_token: str
