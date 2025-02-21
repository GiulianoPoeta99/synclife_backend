from src.api.notes.domain.errors.notes import NotesError, NotesTypeError


class NotesValidator:
    @staticmethod
    def validate_title(title: str) -> str:
        if not title:
            raise NotesError(NotesTypeError.INVALID_TITLE)
        if len(title) > 200:
            raise NotesError(NotesTypeError.TITLE_MAX)
        return title

    @staticmethod
    def validate_content(content: str, title: str) -> str:
        if not content.strip():
            raise NotesError(NotesTypeError.INVALID_CONTENT)
        if len(content) > 2500:
            raise NotesError(NotesTypeError.CONTENT_MAX)
        if len(content.split()) < 1:
            raise NotesError(NotesTypeError.CONTENT_MIN)
        return content

    @staticmethod
    def validate_all(title: str, content: str) -> None:
        NotesValidator.validate_title(title)
        NotesValidator.validate_content(content, title)
