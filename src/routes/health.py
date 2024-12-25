from fastapi import APIRouter, responses
from src import config

router= APIRouter()

@router.get(
    "/status",
    description="Check Midpt APIs health"
)
async def get_health():
    return {
        "environment": config.ENVIRONMENT,
        "version": config.VERSION,
        "status": config.STATUS
    }