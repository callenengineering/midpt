import requests
from src.config import config

async def geocode(address: str) -> tuple:
    GEOCODE_URL=config.GEOCODE_URL
    payload = {
        "address": address,
        "key": config.API_KEY
    }

    response = requests.request("GET", GEOCODE_URL, params=payload).json()
    location = response.get('results')[0]['geometry']['location']
    address_coor = (location.get('lat'), location.get('lng'))
    return address_coor


async def places(location: str, max_radius: int, destination_type: str):
    PLACES_URL= config.PLACES_URL
    payload = {
        "radius": max_radius,
        "type": destination_type,
        "location": location,
        "key": config.API_KEY
    }

    response = requests.request("GET", PLACES_URL, params=payload).json()
    results = response.get('results')
    return results