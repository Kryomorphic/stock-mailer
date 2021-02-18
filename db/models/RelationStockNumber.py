from db.models.Base import Base
from sqlalchemy import Column, Integer, String


class RelationStockNumber(Base):
    __tablename__ = 'relation_stock_number'

    id = Column(Integer, primary_key=True)
    stock_ticker = Column(String(50))
    phone_number = Column(String(50))
    enabled = Column(Integer)
