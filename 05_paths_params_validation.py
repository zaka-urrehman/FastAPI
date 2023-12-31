from typing import Annotated,Dict,List

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: str,
):
    results : Dict[int|str , int|str]  = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results