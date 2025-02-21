from dataclasses import dataclass
from typing import List


@dataclass
class AddTagsDTO:
    note_id: str
    tags: List[str]
    session_token: str
