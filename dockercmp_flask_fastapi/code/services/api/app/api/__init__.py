"""create_app"""
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


def create_app() -> FastAPI:
    """factory method for api"""
    app = FastAPI()

    @app.get("/")
    def root():
        return {"message": "Hello Worldz"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

    return app
