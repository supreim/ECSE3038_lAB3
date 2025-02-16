from uuid import UUID
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    id: UUID


app = FastAPI()


@app.get("/tank/")
async def create_item(item: Item):
    return item
@app.get("/tank/{id}")
async def create_item(item: Item):
    return item

@app.post("/tank/")
async def create_item(item: Item):
    return item

@app.patch("/tank/{id}")
async def create_item(item: Item):
    return item

@app.delete("/tank/{id}")
async def create_item(item: Item):
    return item