from typing import List
from fastapi import APIRouter, responses
from loguru import logger

from src.services import geocode, calculate_midpoint, places

router= APIRouter()

@router.post(
    "/find",
    description="Find the midpoint"
)
async def find_midpoint(
    data: dict = {"addresses": []},
    destination_type: str = "",
    max_radius: int = 2000
):
    '''
    {"addresses": [
        "1600 Pennsylvannia AVE NW, Washington, DC", 
        "20 West 34th Street, New York City, NY"
        ]
    }
    '''
    coordinates: List = []
    for address in data.get('addresses'):
        coor = await geocode(address)
        coordinates.append(coor)

    midpoint = await calculate_midpoint(coordinates)
    location = f"{midpoint[0]}, {midpoint[1]}"
    results = await places(location, max_radius, destination_type)
    
    filtered = []
    for result in results:
        item = {}
        # TODO: change this to to loop through a dictionary
        item['name'] = result.get('name')
        item['address'] = result.get('vicinity')
        item['bussiness_status'] = result.get('business_status')
        item['opening_hours'] = result.get('opening_hours')
        item['types'] = result.get('types')
        item['location'] = result.get('location')
        filtered.append(item)

    output = {
        "midpoint": f"{round(midpoint[0], 3)}, {round(midpoint[1], 3)}",
        "results": filtered
    }

    return output