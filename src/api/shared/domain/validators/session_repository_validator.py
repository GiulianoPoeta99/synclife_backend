from src.api.shared.domain.errors import (
    SessionRepositoryError,
    SessionRepositoryTypeError,
)
from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.value_objects import Uuid


class SessionRepositoryValidator:
    @staticmethod
    def validate_permission(user_request_id: Uuid, id: Uuid) -> None:
        if user_request_id != id:
            raise SessionRepositoryError(SessionRepositoryTypeError.INVALID_USER)

    # TODO: verificar si este metodo es async o no
    @staticmethod
    def validate_session_token(
        session_repository: SessionRepository, session_token: str
    ) -> str:
        user_id = session_repository.get_user_from_session(session_token)
        if not user_id:
            raise SessionRepositoryError(SessionRepositoryTypeError.INVALID_SESSION)
        return user_id
