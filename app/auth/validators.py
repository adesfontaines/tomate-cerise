import re

from app.auth.errors import ValidationError

EMAIL_RE = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$")


def validate_email(raw: str) -> str:
    """Valide une adresse email et la retourne."""
    if not EMAIL_RE.match(raw):
        raise ValidationError("INVALID_EMAIL_FORMAT", field="email")
    return raw
