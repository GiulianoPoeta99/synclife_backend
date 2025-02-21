from dataclasses import dataclass


@dataclass
class ViewTagDto:
    tag_uuid: str
    session_token: str
