from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

tanks = []
class Tank(BaseModel):
    id: str = Field(default_factory=uuid4)
    location: str
    lat: str
    long: str

class Updated_tank(BaseModel):
    location: str | None=None
    lat: str | None=None
    long: str | None=None

app = FastAPI()


@app.get("/tank/", status_code=status.HTTP_200_OK)
async def create_item():
    return tanks

@app.get("/tank/{id}", status_code=status.HTTP_200_OK)
async def create_item(id:str):
    for tank in tanks:
        if id == str(tank.id):
            return tank
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/tank/", status_code=status.HTTP_201_CREATED)
async def create_item(t: Tank):
    if not (t.location and t.lat and t.long):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Missing field value")
    else:
        tanks.append(t)
        return t
    
    
@app.patch("/tank/{id}", status_code=status.HTTP_200_OK)
async def create_item(t:Updated_tank, id: str):
    for i, tank in enumerate(tanks):
        if id == str(tank.id):
            tanks[i].location = t.location if t.location else tanks[i].location
            tanks[i].lat = t.lat if t.lat else tanks[i].lat
            tanks[i].long = t.long if t.long else tanks[i].long
            return tanks[i]
    raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail="Item not found")

@app.delete("/tank/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def create_item(id:str):
    for i, tank in enumerate(tanks):
        if id == str(tank.id):
            tanks.pop(i)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
            