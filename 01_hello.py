"""
This is a basic FastAPI application that defines a single endpoint.

- Endpoint: /
- Method: GET
- Description: Returns a simple "Hello World" message.

Usage:
- Run the FastAPI application using a web server like uvicorn.
- Open the documentation at http://127.0.0.1:8000/docs to interact with the API.

"""

from fastapi import FastAPI


# Create a FastAPI instance
app = FastAPI()

@app.get('/')
def home():
    """
    Home Endpoint

    Returns a simple "Hello World" message.

    Parameters:
    - None
    """
    return "Hello World"



