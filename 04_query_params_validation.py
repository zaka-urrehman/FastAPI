from typing import Annotated,List, Dict
from fastapi import FastAPI, Query

app = FastAPI()




@app.get("/items/")
# notice how Query() is used inside the Annotated. This allow us for additional validation of query strings
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None 
):
    results: Dict[str,List[Dict[str,str]] | str] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results