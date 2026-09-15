import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.auth.errors import ValidationError
from app.auth.validators import validate_email
from app.models.user import DEMO_USER

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    user_email: str


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest) -> LoginResponse:
    try:
        email = validate_email(payload.email)
    except ValidationError as exc:
        logger.exception("Authentication validation failed", extra={"error_code": exc.code})
        try:
            import sentry_sdk
            sentry_sdk.set_tag("validation_code", exc.code)
            sentry_sdk.set_extra("email", payload.email)
            sentry_sdk.capture_exception(exc)
        except ImportError:
            pass
        raise HTTPException(status_code=422, detail={"code": exc.code, "field": exc.field}) from exc

    if email != DEMO_USER.email or payload.password != "demo-password":
        logger.warning("Login rejected: account not found", extra={"email": payload.email})
        try:
            import sentry_sdk
            sentry_sdk.set_tag("auth_error", "ACCOUNT_NOT_FOUND")
            sentry_sdk.set_extra("email", payload.email)
            sentry_sdk.capture_message("ACCOUNT_NOT_FOUND", level="error")
        except ImportError:
            pass
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return LoginResponse(access_token="demo-session-token", user_email=DEMO_USER.email)
