import reflex as rx
import os

class ReflextemplateConfig(rx.Config):
    pass

config = ReflextemplateConfig(
    app_name="myapp",
    telemetry_enabled=False,
    frontend_port=os.getenv("PORT", 3000),
    backend_port=os.getenv("PORT", 8000),
    backend_host="0.0.0.0",
    api_url=os.getenv("API_URL", "http://127.0.0.1:8000")
)