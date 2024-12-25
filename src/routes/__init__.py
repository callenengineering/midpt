from fastapi import APIRouter

from . import health
from . import midpoint

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(midpoint.router, prefix="/midpoint", tags=["midpoint"])