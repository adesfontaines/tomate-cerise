from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    email: str
    display_name: str
    role: str = "customer"


DEMO_USER = User(
    email="ade@softfluent.com",
    display_name="Adé",
)
