import os
from fastapi import FastAPI

from .routes import api_router

app = FastAPI(
    title="Midpt API",
    description="Find the midpoint between multiple locations",
)

app.include_router(api_router)
