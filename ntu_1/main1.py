from pydantic import BaseModel
from fastapi import FastAPI, Body, Query
from typing import Annotated


app = FastAPI()


class Car(BaseModel):
    fuel: str
    transmission: str
    size: str


class Item(BaseModel):
    name: str
    price: float | None = 2.5
    quantity: int = 1


@app.get("/")
def get_route():
    return {"message": "Hello World"}


# @app.post("/route")
# def get_routes(newCar: Annotated[str, Query(max_length=5, min_length=3, pattern=["^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"])]):
#     return newCar


@app.post('/data')
def add_data(item: Item|None = None, car: Car|None = None)->list:
    return [
        item,
        car
    ]
