from datetime import timedelta
from typing import Optional

import redis

from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.value_objects import Uuid
from src.api.shared.infrastructure.persistence import get_dragonfly_connection


class DragonflySessionRepository(SessionRepository):
    def __init__(self, client: redis.Redis):
        self.__client = client
        self.__session_duration = timedelta(hours=24)

    @staticmethod
    def get_repository() -> "DragonflySessionRepository":
        return DragonflySessionRepository(get_dragonfly_connection())

    def create_session(self, user_id: Uuid) -> str:
        session_token = str(Uuid())
        self.__client.setex(
            session_token, int(self.__session_duration.total_seconds()), str(user_id)
        )
        return session_token

    def get_user_from_session(self, session_token: str) -> Optional[str]:
        user = str(self.__client.get(session_token))
        return user if user else None

    def delete_session(self, session_token: str) -> None:
        self.__client.delete(session_token)
