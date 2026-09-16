import re

from app.auth.errors import ValidationError

EMAIL_RE = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$")


def validate_email(raw: str) -> str:
    """Valide et normalise une adresse email pour la comparaison de compte."""
    normalized = raw.strip().lower()
    local_part, separator, domain = normalized.partition("@")
    if separator and domain == "softfluent.com":
        local_part = local_part.replace(".", "").split("+", 1)[0]
        normalized = f"{local_part}@{domain}"
    if not EMAIL_RE.fullmatch(normalized):
        raise ValidationError("INVALID_EMAIL_FORMAT", field="email")
    return normalized
