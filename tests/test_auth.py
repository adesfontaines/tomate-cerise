from fastapi.testclient import TestClient

from app.auth.errors import ValidationError
from app.auth.validators import validate_email
from app.main import app


client = TestClient(app)


def test_validate_standard_email():
    assert validate_email("ade@softfluent.com") == "ade@softfluent.com"


def test_validate_email_without_at_sign():
    try:
        validate_email("ade.softfluent.com")
    except ValidationError as exc:
        assert exc.code == "INVALID_EMAIL_FORMAT"
        assert exc.field == "email"
    else:
        raise AssertionError("Expected ValidationError")


def test_validate_empty_email():
    try:
        validate_email("")
    except ValidationError as exc:
        assert exc.code == "INVALID_EMAIL_FORMAT"
    else:
        raise AssertionError("Expected ValidationError")


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_demo_login_page_is_available():
    response = client.get("/demo")
    assert response.status_code == 200
    assert "Tomate Cerise" in response.text
    assert "Se connecter" in response.text



def test_landing_page_is_available():
    response = client.get("/")
    assert response.status_code == 200
    assert "Des paniers frais" in response.text
    assert "Découvrir mon espace" in response.text
    assert "/static/hero-baskets.png" in response.text



def test_login_with_demo_user():
    response = client.post(
        "/api/v1/auth/login",
        json={"email": "ade@softfluent.com", "password": "demo-password"},
    )
    assert response.status_code == 200
