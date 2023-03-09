from typing import List
from sqlalchemy.orm import Session
from schemas.schema import CreateAndUpdateBtc, Btc
from models.btc_price import BtcPrice
import requests


# Path: controllers/btc.py

def get_all_btc(db: Session):
    return db.query(BtcPrice).all()

def get_btc_by_id(id: int, db: Session):
    return db.query(BtcPrice).filter(BtcPrice.id == id).first()

def create_btc(btc: CreateAndUpdateBtc, db: Session):
    db_btc = BtcPrice(price=btc.price)
    db.add(db_btc)
    db.commit()
    db.refresh(db_btc)
    return db_btc


def fetch_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.request("GET", url)
    return response.json()['bitcoin']['usd']


 