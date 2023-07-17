from .database import Base
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP
from sqlalchemy.sql import func


class Inquilino(Base):
    __tablename__ = "inquilinos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(Integer, nullable=False)
    data_nascimento = Column(Date, nullable=True)
    cidade = Column(String, nullable=True)
    estado = Column(String, nullable=True)
    email = Column(String, nullable=True)
    ultima_alteracao = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
