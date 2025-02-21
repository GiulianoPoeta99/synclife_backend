from dataclasses import dataclass
from datetime import date


@dataclass
class UpdateItemDto:
    inventory_id: str
    product_name: str
    amount: int
    expiration_date: date
    session_token: str
