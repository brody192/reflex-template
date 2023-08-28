import reflex as rx
import os

railway_domain = "RAILWAY_PUBLIC_DOMAIN"

url = f'https://{os.getenv(railway_domain)}' if railway_domain in os.environ else "http://127.0.0.1:8000"

print(url)

class ReflextemplateConfig(rx.Config):
    pass

config = ReflextemplateConfig(
    app_name="myapp",
    telemetry_enabled=False,
    frontend_port=os.getenv("PORT", 3000),
    backend_port=os.getenv("PORT", 8000),
    backend_host="0.0.0.0",
    api_url=f'https://{os.getenv(railway_domain)}' if railway_domain in os.environ else "http://127.0.0.1:8000"
)

# os.getenv("API_URL", "http://127.0.0.1:8000")