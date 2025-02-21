from src.api.notes.domain.errors.tags import TagsError, TagsTypeError


class TagsValidator:
    @staticmethod
    def validate_name(name: str) -> str:
        if not name:
            raise TagsError(TagsTypeError.INVALID_NAME)
        if len(name) > 200:
            raise TagsError(TagsTypeError.NAME_MAX)
        return name

    @staticmethod
    def validate_all(name: str) -> None:
        TagsValidator.validate_name(name)
