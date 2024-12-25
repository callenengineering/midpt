import pytest
from src import routes

@pytest.mark.asyncio
async def test_get_health():
    result = await routes.health.get_health()
    print(result)
    assert "environment" in result.keys()
    assert "version" in result.keys()
    assert "status" in result.keys()