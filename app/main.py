from fastapi import Depends, FastAPI
from controllers.btc import fetch_btc_price
from router import btc
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from schemas.schema import Btc
app = FastAPI()
from models import btc_price
from database import SessionLocal, db_engine, get_db
from fastapi_utils.tasks import repeat_every


btc_price.Base.metadata.create_all(bind=db_engine)

app.include_router(btc.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
@repeat_every(seconds=60)
def fetch_btc_price_and_save():
    try:
        print("fetching btc price")
        price = fetch_btc_price()
        print(btc_price)
        db_btc = btc_price.BtcPrice(price=price) 
        db = SessionLocal()
        db.add(db_btc)
        db.commit()
    except Exception as e:
        print(e)    


@app.get("/")
async def root():
    return {"message": "Hello World"}