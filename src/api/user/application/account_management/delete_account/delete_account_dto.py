from dataclasses import dataclass


@dataclass
class DeleteAccountDto:
    uuid: str
    session_token: str
