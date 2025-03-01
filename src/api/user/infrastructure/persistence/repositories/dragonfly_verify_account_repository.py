from datetime import timedelta
from typing import Optional

import redis

from src.api.shared.domain.value_objects import Uuid
from src.api.shared.infrastructure.persistence import get_dragonfly_connection
from src.api.user.domain.repositories import VerifyAccountRepository


class DragonflyVerifyAccountRepository(VerifyAccountRepository):
    def __init__(self, client: redis.Redis):
        self.__client = client
        self.__session_duration = timedelta(hours=48)

    @staticmethod
    def get_repository() -> "DragonflyVerifyAccountRepository":
        return DragonflyVerifyAccountRepository(get_dragonfly_connection())

    def create_validation_request(self, user_uuid: Uuid) -> str:
        validate_token = str(Uuid())
        self.__client.setex(
            validate_token, int(self.__session_duration.total_seconds()), str(user_uuid)
        )
        return validate_token

    def find_user_from_validation_request(self, validate_token: str) -> Optional[Uuid]:
        user = str(self.__client.get(validate_token))
        return Uuid(user) if user else None

    def delete_validation_request(self, validation_token: str) -> None:
        self.__client.delete(validation_token)
