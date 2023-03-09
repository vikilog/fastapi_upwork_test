from ast import List
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from controllers.btc import fetch_btc_price, get_all_btc, get_btc_by_id, create_btc
from database import get_db
from schemas.schema import CreateAndUpdateBtc, Btc
from fastapi_utils.cbv import cbv
from models.btc_price import BtcPrice
router = APIRouter()

@cbv(router)
class Btc:
    session: Session = Depends(get_db)

    @router.get("/btc")
    def get_all_btc(self):
        return get_all_btc(self.session)
    
    @router.get("/btc/{id}")
    def get_btc_by_id(self, id: int):
        return get_btc_by_id(id, self.session)
    
    @router.post("/btc")
    def create_btc(self, btc: CreateAndUpdateBtc):
        return create_btc(btc, self.session)
    
