# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = 0.0


# item = Item(name="apple", description="red fruit", price=5.5)
# item_json = item.json()
# # item = Item.parse_raw(item_json)
# print(item_json)

from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()


class User(BaseModel):
    name: str
    age: int

    @validator("age")
    def check_user_age(cls, v):
        if v < 18:
            raise ValueError("Age must be at least 18")
        return v


user = User(name="hyeongbin", age=17)
print(user)
