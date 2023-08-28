import reflex as rx
import os

railway_domain = "RAILWAY_PUBLIC_DOMAIN"

class ReflextemplateConfig(rx.Config):
    pass

config = ReflextemplateConfig(
    app_name="myapp",
    telemetry_enabled=False,
    frontend_port=3000,
    backend_port=8000,
    backend_host="0.0.0.0",
    api_url=f'https://{os.environ[railway_domain]}/backend' if railway_domain in os.environ else "http://127.0.0.1:8000"
)