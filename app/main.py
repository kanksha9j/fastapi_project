from http.client import HTTPException
from typing import Union

from fastapi import FastAPI
from sentry_sdk import set_user

from app.charging_station import ChargingStationCreate
from app.charging_station import ChargingStation
from app.db import get_db_connection

app = FastAPI()

# An API endpoint is the specific URL (including parameters) that a client can call to interact with your backend.
# eg: http://localhost:8000/items/42
# This defines a route. The route is the combination of path + http method(GET, POST, PUT) + handler function.
# Path = /
# Method = GET
# Handler = read_root() function
# This route means: "When someone sends a GET request to /, run read_root()."
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Dynamic routes. You can capture path parameters. 
# /items/42 → item_id = 42. Route has a variable in the path.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/status")
async def status():
    return {"message": "OK"}

@app.post("/charging_stations/")
def create_charging_station(station: ChargingStationCreate):
    conn, cursor = get_db_connection()
    try:
        cursor.execute("INSERT INTO charging_station (name, latitude, longitude, address) VALUES (%s, %s, %s, %s) RETURNING *", (station.name, station.latitude, station.longitude, station.address))
        new_station = cursor.fetchone()
        conn.commit()
        cursor.close()
        
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))

    conn.close()
    if new_station:
        return ChargingStation(**new_station)

    raise HTTPException(status_code=400, detail="Charging station creation failed")