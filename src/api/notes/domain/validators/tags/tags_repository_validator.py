from typing import Optional

from src.api.notes.domain.entities.tags import Tags
from src.api.notes.domain.errors.tags import TagsError, TagsTypeError
from src.api.notes.domain.repositories.tags_repository import TagsRepository
from src.api.shared.domain.value_objects import Uuid


class TagsRepositoryValidator:
    @staticmethod
    def tag_found(tag: Optional[Tags]) -> Tags:
        if tag is None:
            raise TagsError(TagsTypeError.TAG_NOT_FOUND)
        return tag

    @staticmethod
    def user_owns_tag(repository: TagsRepository, user_id: Uuid, tag_id: Uuid) -> None:
        tag = repository.find_by_id(tag_id)
        if tag is None or tag.user_id != user_id:
            raise TagsError(TagsTypeError.TAG_NOT_OWNED)

    @staticmethod
    def tag_name_unique(repository: TagsRepository, name: str, user_id: Uuid) -> None:
        if repository.find_by_name_and_user_id(name, user_id):
            raise TagsError(TagsTypeError.DUPLICATED_NAME)
