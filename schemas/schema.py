# schemas.py
from pydantic import BaseModel




# TO support creation and update APIs
class CreateAndUpdateBtc(BaseModel):
    price: int


# TO support list and get APIs
class Btc(CreateAndUpdateBtc):
    id: int

    class Config:
        orm_mode = True


