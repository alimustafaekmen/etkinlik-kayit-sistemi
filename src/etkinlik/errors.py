"""Servislerin fırlattığı hatalar. Hata yakalayıcı bunları HTTP koduna çevirir."""


class ServiceError(Exception):
    status_code = 400
    code = "service_error"

    def __init__(self, message: str, details: dict | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> dict:
        body = {"error": self.code, "message": self.message}
        if self.details:
            body["details"] = self.details
        return body


class ValidationError(ServiceError):
    code = "validation_error"


class NotFoundError(ServiceError):
    status_code = 404
    code = "not_found"


class CapacityFullError(ServiceError):
    status_code = 409
    code = "capacity_full"


class DuplicateRegistrationError(ServiceError):
    status_code = 409
    code = "duplicate_registration"
