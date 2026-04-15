"""Common exceptions."""


class AppError(Exception):
    """Base application error."""


class NotFoundError(AppError):
    """Raised when a requested resource does not exist."""


class ExternalServiceError(AppError):
    """Raised when an external service call fails."""
