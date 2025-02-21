from src.api.v1.shared.infrastructure.http.decorators import handle_exceptions
from src.api.v1.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
)
from src.api.v1.user.application.authentication.login import LoginUseCase
from src.api.v1.user.application.authentication.register import RegisterUseCase
from src.api.v1.user.infrastructure.http.dtos.login import (
    PydanticLoginRequestDto,
    PydanticLoginResponseDto,
)
from src.api.v1.user.infrastructure.http.dtos.register import (
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
)
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
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()
        use_case = RegisterUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application()
        user, session_token = use_case.execute(app_dto)

        return PydanticRegisterResponseDto(
            user=SqlModelUserModel.from_entity(user),
            session_token=session_token,
        )

    @staticmethod
    @handle_exceptions
    async def login(request_dto: PydanticLoginRequestDto) -> PydanticLoginResponseDto:
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()
        use_case = LoginUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application()
        user, session_token = use_case.execute(app_dto)

        return PydanticLoginResponseDto(
            user=SqlModelUserModel.from_entity(user),
            session_token=session_token,
        )
