from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func

from data.models.BaseModel import EntityMeta


class Renter(EntityMeta):
    __tablename__ = "renters"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    birth_date = Column(Date, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    email = Column(String, nullable=True)
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
