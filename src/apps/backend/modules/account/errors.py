from modules.account.types import AccountErrorCode
from modules.error.custom_errors import AppError


class AccountWithUserNameExistsError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(code=AccountErrorCode.USERNAME_ALREADY_EXISTS, http_status_code=409, message=message)


class AccountNotFoundError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(code=AccountErrorCode.NOT_FOUND, http_status_code=404, message=message)


class AccountInvalidPasswordError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(code=AccountErrorCode.INVALID_CREDENTIALS, http_status_code=401, message=message)


class AccountBadRequestError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(code=AccountErrorCode.BAD_REQUEST, http_status_code=400, message=message)


class AccountWithPhoneNumberExistsError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(code=AccountErrorCode.PHONE_NUMBER_ALREADY_EXISTS, http_status_code=409, message=message)
