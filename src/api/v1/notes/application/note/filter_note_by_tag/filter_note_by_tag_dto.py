from dataclasses import dataclass


@dataclass
class FilterNotesByTagDTO:
    tag_id: str
