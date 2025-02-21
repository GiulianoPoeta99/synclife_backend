from dataclasses import dataclass


@dataclass
class RemoveTagDTO:
    note_id: str
    tag_id: str
    session_token: str
