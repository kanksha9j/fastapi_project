from pydantic import BaseModel

class ChargingStationCreate(BaseModel):
    station_id: int
    name: str
    latitude: float
    longitude: float
    address: str

class ChargingStation(ChargingStationCreate):
    station_id: int