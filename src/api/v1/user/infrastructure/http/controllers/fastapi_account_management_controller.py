from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.application import (
    ChangePasswordUseCase,
    ChangePersonalInformationUseCase,
    DeleteAccountUseCase,
    ViewAccountUseCase,
)
from src.api.v1.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.v1.user.domain.value_objects import Email
from src.api.v1.user.infrastructure.http.decorators import handle_exceptions
from src.api.v1.user.infrastructure.http.dtos import (
    PydanticChangePasswordRequestDto,
    PydanticChangePasswordResponseDto,
    PydanticChangePersonalInformationRequestDto,
    PydanticChangePersonalInformationResponseDto,
    PydanticDeleteAccountRequestDto,
    PydanticDeleteAccountResponseDto,
    PydanticViewAccountRequestDto,
    PydanticViewAccountResponseDto,
)
from src.api.v1.user.infrastructure.http.services.in_memory_session_service import (
    InMemorySessionService,
)
from src.api.v1.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)
from src.api.v1.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)


class FastApiAccountManagementController:
    @staticmethod
    @handle_exceptions
    async def view_account(
        request_dto: PydanticViewAccountRequestDto, user_request_id: str
    ) -> PydanticViewAccountResponseDto:
        repository = SqlModelUserRepository.get_repository()
        InMemorySessionService.validate_permission(
            Uuid(user_request_id), Uuid(request_dto.uuid)
        )

        use_case = ViewAccountUseCase(repository)
        app_dto = request_dto.to_application()
        user = use_case.execute(app_dto)

        return PydanticViewAccountResponseDto(user=SqlModelUserModel.from_entity(user))

    @staticmethod
    @handle_exceptions
    async def delete_account(
        request_dto: PydanticDeleteAccountRequestDto, user_request_id: str
    ) -> PydanticDeleteAccountResponseDto:
        repository = SqlModelUserRepository.get_repository()
        InMemorySessionService.validate_permission(
            Uuid(user_request_id), Uuid(request_dto.uuid)
        )

        use_case = DeleteAccountUseCase(repository)
        app_dto = request_dto.to_application()
        user = use_case.execute(app_dto)

        return PydanticDeleteAccountResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )

    @staticmethod
    @handle_exceptions
    async def change_password(
        request_dto: PydanticChangePasswordRequestDto, user_request_id: str
    ) -> PydanticChangePasswordResponseDto:
        repository = SqlModelUserRepository.get_repository()
        validation_user = repository.find_by_email(Email(request_dto.email))

        if validation_user is None:
            raise UserRepositoryError(UserRepositoryTypeError.USER_NOT_FOUND)

        InMemorySessionService.validate_permission(
            Uuid(user_request_id), validation_user.uuid
        )

        use_case = ChangePasswordUseCase(repository)
        app_dto = request_dto.to_application()
        user = use_case.execute(app_dto)

        return PydanticChangePasswordResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )

    @staticmethod
    @handle_exceptions
    async def change_personal_information(
        request_dto: PydanticChangePersonalInformationRequestDto, user_request_id: str
    ) -> PydanticChangePersonalInformationResponseDto:
        repository = SqlModelUserRepository.get_repository()
        InMemorySessionService.validate_permission(
            Uuid(user_request_id), Uuid(request_dto.uuid)
        )

        use_case = ChangePersonalInformationUseCase(repository)
        app_dto = request_dto.to_application()
        user = use_case.execute(app_dto)

        return PydanticChangePersonalInformationResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )
