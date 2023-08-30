# Welcome to Reflex! This file outlines the steps to create a basic app

import reflex as rx

from .pages import index
from .pages import health
from .pages import not_found

from .api import root

app = rx.App()

app.add_page(index)
app.add_page(health)

app.api.add_api_route(
    path="/",
    endpoint=root
)

not_found_text = "The page you were looking for could not be found"

app.add_custom_404_page(
    title="404 - Page Not Found", 
    description=not_found_text,
    component=not_found(not_found_text)
)

app.compile()
