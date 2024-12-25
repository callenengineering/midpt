from typing import List

async def calculate_midpoint(coordinates: List) -> tuple:
    n = len(coordinates)
    xi = [coordinate[0] for coordinate in coordinates]
    yi = [coordinate[1] for coordinate in coordinates]
    midpoint = (1/n*sum(xi), 1/n*sum(yi))
    return midpoint

