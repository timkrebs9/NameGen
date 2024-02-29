from fastapi import FastAPI
from faker import Faker
from typing import List
from pydantic import BaseModel
import uvicorn


app = FastAPI()
fake = Faker()

class User(BaseModel):
    name: str
    email: str
    address: str
    phone_number: str

@app.get("/users", response_model=List[User])
async def read_users(count: int = 5):
    users = []
    for _ in range(count):
        user = User(
            name=fake.name(),
            email=fake.email(),
            address=fake.address(),
            phone_number=fake.phone_number(),
        )
        users.append(user)
    return users


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

