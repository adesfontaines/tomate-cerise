import os

import sentry_sdk
from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.web import demo_login_page


sentry_sdk.init(
    dsn="https://258ec61268597df76316fa0ba51dc3dc@o4508075121901568.ingest.de.sentry.io/4512092357853264",
    send_default_pii=True,
    enable_logs=True,
    traces_sample_rate=1.0,
    profile_session_sample_rate=1.0,
    profile_lifecycle="trace",
)

app = FastAPI(title="Tomate Cerise API", version="1.0.0")
app.include_router(auth_router)
app.add_api_route("/demo", demo_login_page, methods=["GET"], include_in_schema=False)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "environment": os.getenv("APP_ENV", "development")}
