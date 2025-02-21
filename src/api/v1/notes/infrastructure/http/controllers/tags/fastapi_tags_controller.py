from src.api.v1.notes.application.tag.create_tag import CreateTagUseCase
from src.api.v1.notes.application.tag.delete_tag import DeleteTagUseCase
from src.api.v1.notes.application.tag.update_tag import UpdateTagUseCase
from src.api.v1.notes.application.tag.view_all_tags import ViewAllTagsUseCase
from src.api.v1.notes.application.tag.view_all_tags.view_all_tags_dto import (
    ViewAllTagsDto,
)
from src.api.v1.notes.application.tag.view_tag import ViewTagUseCase
from src.api.v1.notes.infrastructure.http.dtos.tags import (
    PydanticCreateTagRequestDto,
    PydanticCreateTagResponseDto,
    PydanticDeleteTagRequestDto,
    PydanticDeleteTagResponseDto,
    PydanticUpdateTagsRequestDto,
    PydanticUpdateTagsResponseDto,
    PydanticViewAllTagsResponseDto,
    PydanticViewTagsRequestDto,
    PydanticViewTagsResponseDto,
)
from src.api.v1.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SqlModelTagsModel,
)
from src.api.v1.notes.infrastructure.persistence.repositories.sqlmodel_tags_repository import (  # noqa: E501
    SQLModelTagsRepository,
)
from src.api.v1.shared.infrastructure.http.decorators import handle_exceptions
from src.api.v1.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
)
from src.api.v1.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)


class FastApiTagsController:
    @staticmethod
    @handle_exceptions
    async def create(
        request_dto: PydanticCreateTagRequestDto, session_token: str
    ) -> PydanticCreateTagResponseDto:
        tag_repo = SQLModelTagsRepository.get_repository()
        user_repo = SqlModelUserRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = CreateTagUseCase(tag_repo, user_repo, session_repo)
        dto = request_dto.to_application(session_token)
        tag = use_case.execute(dto)

        return PydanticCreateTagResponseDto(tag=SqlModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def update(
        request_dto: PydanticUpdateTagsRequestDto, session_token: str
    ) -> PydanticUpdateTagsResponseDto:
        tag_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = UpdateTagUseCase(tag_repo, session_repo)
        dto = request_dto.to_application(session_token)
        tag = use_case.execute(dto)

        return PydanticUpdateTagsResponseDto(tag=SqlModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteTagRequestDto, session_token: str
    ) -> PydanticDeleteTagResponseDto:
        tag_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = DeleteTagUseCase(tag_repo, session_repo)
        dto = request_dto.to_application(session_token)
        tag = use_case.execute(dto)

        return PydanticDeleteTagResponseDto(tag=SqlModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def view(
        request_dto: PydanticViewTagsRequestDto, session_token: str
    ) -> PydanticViewTagsResponseDto:
        tag_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewTagUseCase(tag_repo, session_repo)
        dto = request_dto.to_application(session_token)
        tag = use_case.execute(dto)

        return PydanticViewTagsResponseDto(tag=SqlModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def view_all(session_token: str) -> PydanticViewAllTagsResponseDto:
        tag_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewAllTagsUseCase(tag_repo, session_repo)

        dto = ViewAllTagsDto(session_token=session_token)
        tags = use_case.execute(dto)

        response_tags = []
        for tag in tags:
            model_tag = SqlModelTagsModel.from_entity(tag)
            response_tags.append(model_tag)

        return PydanticViewAllTagsResponseDto(tags=response_tags)
