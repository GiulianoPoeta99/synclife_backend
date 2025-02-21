from dataclasses import dataclass


@dataclass
class ViewAccountDto:
    uuid: str
    session_token: str
