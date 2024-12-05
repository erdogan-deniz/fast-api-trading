from enum import Enum
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError

# Crea application:
app = FastAPI(title="Trading application")


# Handler to show errors user:
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]

new_fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    amount: float
    price: float = Field(ge=0)
    side: str = Field(max_length=5)


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    name: str
    create_data: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: [Degree] | None = []


@app.get("/users/{user_id}", response_model=list[User])
def get_data(user_id: int):
    return {"ID": [taked_id for taked_id in fake_users if taked_id.get("id") == user_id]}


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 1) -> list:
    return fake_trades[offset:][:limit]


@app.post("/trades")
def add_trades(trades: list[Trade]):
    trades.extend(trades)

    return {"Status": 200, "data": trades}


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str) -> dict:
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    current_user["name"] = new_name

    return {"Status": f"Name has been changed on {new_name}"}
