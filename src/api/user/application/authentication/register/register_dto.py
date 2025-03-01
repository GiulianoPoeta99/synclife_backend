from dataclasses import dataclass
from datetime import date


@dataclass
class RegisterDTO:
    email: str
    password: str
    first_name: str
    last_name: str
    birth_date: date
    phone: str
    url: str
