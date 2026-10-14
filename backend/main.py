from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Footstep(BaseModel):
    device: str
    zone: str
    rssi: int
    location: str
    timestamp: str

@app.post("/footsteps/")
async def log_footstep(footstep: Footstep):
    print(f"📍 {footstep.timestamp} | {footstep.location} | {footstep.zone} | {footstep.rssi}")
