import os
import json
from shapely.geometry import Point, Polygon
from fastapi import APIRouter, Query
from shapely.ops import nearest_points
from math import radians, cos, sin, asin, sqrt

router = APIRouter()

ROUTE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "route"))
polygons = {}

for filename in os.listdir(ROUTE_DIR):
    if filename.endswith(".json"):
        filepath = os.path.join(ROUTE_DIR, filename)
        with open(filepath, "r") as f:
            data = json.load(f)
            coords = [(lon, lat) for lat, lon in data["polygon"]]
            if len(coords) > 2:
                polygons[filename] = Polygon(coords)

def haversine(lon1, lat1, lon2, lat2):
    R = 6371000
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * asin(min(1, sqrt(a)))
    return R * c

@router.get("/")
def root():
    return {"message": "GPS Polygon API running", "routes_loaded": len(polygons)}

@router.get("/check")
def check_point(coord: str = Query(..., description="Format: lat,lon")):
    try:
        lat, lon = map(float, coord.split(","))
    except ValueError:
        return {"error": "Invalid coord format, use lat,lon"}

    point = Point(lon, lat)

    def clean_name(name: str):
        return name[:-5] if name.endswith(".json") else name

    for route_name, poly in polygons.items():
        if poly.contains(point):
            return {"in_area": True, "route": clean_name(route_name)}

    min_distance_m = float("inf")
    nearest_route = None

    for route_name, poly in polygons.items():
        nearest_geom = nearest_points(poly, point)[0]
        dist_m = haversine(point.x, point.y, nearest_geom.x, nearest_geom.y)
        if dist_m < min_distance_m:
            min_distance_m = dist_m
            nearest_route = route_name

    return {
        "in_area": False,
        "nearest_route": clean_name(nearest_route) if nearest_route else None,
        "distance_m": round(min_distance_m, 2)
    }
