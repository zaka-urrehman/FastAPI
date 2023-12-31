from fastapi import FastAPI


# Create a FastAPI instance
app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None): 
    """
    Read Item Endpoint

    Parameters:
    - item_id (int): Path Patameter (The unique identifier of the item)
    - q (str, optional): An optional query parameter. Default is None.

    """
    return {"item_id": item_id, "q": q}
