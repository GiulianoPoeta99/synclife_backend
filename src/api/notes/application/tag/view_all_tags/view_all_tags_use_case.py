from typing import List

from src.api.notes.application.tag.view_all_tags.view_all_tags_dto import ViewAllTagsDto
from src.api.notes.domain.entities.tags import Tags
from src.api.notes.domain.repositories.tags_repository import TagsRepository
from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects.uuid import Uuid


class ViewAllTagsUseCase:
    def __init__(
        self, tag_repository: TagsRepository, session_repository: SessionRepository
    ):
        self.__tag_repository = tag_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAllTagsDto) -> List[Tags]:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        tag = self.__tag_repository.find_all_by_user_id(Uuid(user_request_uuid))

        return tag
