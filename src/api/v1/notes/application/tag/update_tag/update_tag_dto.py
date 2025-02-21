from dataclasses import dataclass


@dataclass
class UpdateTagDto:
    tag_id: str
    name: str
    session_token: str
