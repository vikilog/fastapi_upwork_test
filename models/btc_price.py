from sqlalchemy.schema import Column
from sqlalchemy.types import Integer,DATETIME
from database import Base



class BtcPrice(Base):
    __tablename__ = "btc_price"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)

    
