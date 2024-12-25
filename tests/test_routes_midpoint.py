import pytest
from src import routes

@pytest.fixture
def midpoint_destination_type():
    return "hospital"

@pytest.fixture
def midpoint_max_radius():
    return 2000

@pytest.fixture
def midpoint_data():
    return dict(
        addresses=["1600 Pennsylvannia AVE NW, Washington, DC","20 West 34th Street, New York City, NY"]
    )

@pytest.mark.asyncio
async def test_find_midpoint():
    result = await routes.midpoint.find_midpoint(
        destination_type=midpoint_destination_type,
        max_radius=midpoint_max_radius,
        data=dict(
        addresses=["1600 Pennsylvannia AVE NW, Washington, DC","20 West 34th Street, New York City, NY"]
    )
    )
    assert "midpoint" in result.keys()
    assert "results" in result.keys()