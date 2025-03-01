import os

from dotenv import load_dotenv

from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    DragonflySessionRepository,
    MailHogSMTPEmailSenderRepository,
)
from src.api.user.application.authentication.login import LoginUseCase
from src.api.user.application.authentication.register import RegisterUseCase
from src.api.user.application.authentication.verify_account import VerifyAccountUseCase
from src.api.user.infrastructure.http.dtos import (
    PydanticLoginRequestDto,
    PydanticLoginResponseDto,
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
)
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)
from src.api.user.infrastructure.persistence.repositories.dragonfly_verify_account_repository import (  # noqa: E501
    DragonflyVerifyAccountRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)


class FastApiAuthenticationController:
    @staticmethod
    @handle_exceptions
    async def register(
        request_dto: PydanticRegisterRequestDto,
    ) -> PydanticRegisterResponseDto:
        user_repository = SqlModelUserRepository.get_repository()
        user_validation_repository = DragonflyVerifyAccountRepository.get_repository()
        smtp_email_sender_repository = MailHogSMTPEmailSenderRepository.get_repository()

        use_case = RegisterUseCase(
            user_repository, smtp_email_sender_repository, user_validation_repository
        )

        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users"

        app_dto = request_dto.to_application(url=url)
        user = use_case.execute(app_dto)

        return PydanticRegisterResponseDto(
            user=SqlModelUserModel.from_entity(user),
        )

    @staticmethod
    @handle_exceptions
    async def validate_account(
        request_dto: PydanticVerifyAccountRequestDTO,
    ) -> PydanticVerifyAccountResponseDTO:
        user_repository = SqlModelUserRepository.get_repository()
        user_validation_repository = DragonflyVerifyAccountRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = VerifyAccountUseCase(
            user_repository, user_validation_repository, session_repository
        )
        app_dto = request_dto.to_application()
        user, session_token = use_case.execute(app_dto)

        return PydanticVerifyAccountResponseDTO(
            user=SqlModelUserModel.from_entity(user), session_token=session_token
        )

    @staticmethod
    @handle_exceptions
    async def login(request_dto: PydanticLoginRequestDto) -> PydanticLoginResponseDto:
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()
        use_case = LoginUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application()
        user, session_token = use_case.execute(app_dto)

        return PydanticLoginResponseDto(
            user=SqlModelUserModel.from_entity(user),
            session_token=session_token,
        )
