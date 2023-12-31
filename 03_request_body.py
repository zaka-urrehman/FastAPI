# When you need to send data from a client (let's say, a browser) to your API, you send it as a request body
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item



@app.put("/items/{item_id}")
async def create_items(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}