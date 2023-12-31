
# FastAPI

FastAPI is a modern and fast web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use, efficient, and to provide automatic interactive documentation 

## Features
* #### Fast:
 As the name suggests, FastAPI is designed for high performance. It is built on top of Starlette and Pydantic, leveraging their performance-oriented features.

* #### Automatic Documentation:
 FastAPI generates interactive API documentation (using Swagger UI and ReDoc) automatically based on the Python type hints and annotations in your code. This helps developers understand how to use your API without separate documentation.

* #### Validation and Serialization:
FastAPI uses Pydantic models for request and response data validation. This allows for automatic validation of data and automatic generation of OpenAPI and JSON Schema documentation.

* #### Dependency Injection:
FastAPI supports dependency injection, making it easy to manage dependencies and components in your application.

* #### Asynchronous Support:
FastAPI is designed to work seamlessly with asynchronous programming. It allows you to write asynchronous routes and use asynchronous libraries for better performance.

* #### Security:
It includes built-in security features such as OAuth2, API key handling, and more to help secure your API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install fastapi
```

Also install [uvicorn](https://www.uvicorn.org/) as a server 
```bash
pip install 'uvicorn[standard]'
```

You can also add other optional dependencies 