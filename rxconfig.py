import reflex as rx
import os

print(f'https://{os.getenv("API_URL")}' if "API_URL" in os.environ else "http://127.0.0.1:8000")

class ReflextemplateConfig(rx.Config):
    pass

config = ReflextemplateConfig(
    app_name="myapp",
    telemetry_enabled=False,
    frontend_port=os.getenv("PORT", 3000),
    backend_port=os.getenv("PORT", 8000),
    backend_host="0.0.0.0",
    api_url=f'https://{os.getenv("API_URL")}' if "API_URL" in os.environ else "http://127.0.0.1:8000"
)

# os.getenv("API_URL", "http://127.0.0.1:8000")