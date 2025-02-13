from src.api.v1.user.application.authentication.login import LoginUseCase
from src.api.v1.user.application.authentication.register import RegisterUseCase
from src.api.v1.user.infrastructure.http.decorators import handle_exceptions
from src.api.v1.user.infrastructure.http.dtos.login import (
    PydanticLoginRequestDto,
    PydanticLoginResponseDto,
)
from src.api.v1.user.infrastructure.http.dtos.register import (
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
)
from src.api.v1.user.infrastructure.http.services import InMemorySessionService
from src.api.v1.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)
from src.api.v1.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)


class FastApiAuthenticationController:
    @staticmethod
    @handle_exceptions
    async def register(
        request_dto: PydanticRegisterRequestDto,
    ) -> PydanticRegisterResponseDto:
        repository = SqlModelUserRepository.get_repository()
        use_case = RegisterUseCase(repository)
        app_dto = request_dto.to_application()
        user = use_case.execute(app_dto)

        return PydanticRegisterResponseDto(
            user=SqlModelUserModel.from_entity(user),
            session_token=InMemorySessionService.create_session(str(user.uuid)),
        )

    @staticmethod
    @handle_exceptions
    async def login(request_dto: PydanticLoginRequestDto) -> PydanticLoginResponseDto:
        repository = SqlModelUserRepository.get_repository()
        use_case = LoginUseCase(repository)
        app_dto = request_dto.to_application()
        user = use_case.execute(app_dto)

        return PydanticLoginResponseDto(
            user=SqlModelUserModel.from_entity(user),
            session_token=InMemorySessionService.create_session(str(user.uuid)),
        )
