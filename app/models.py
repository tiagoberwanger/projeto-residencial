from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base
from schemas import TiposEnum, StatusEnum


class Inquilino(Base):
    __tablename__ = "inquilinos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    data_nascimento = Column(Date, nullable=True)
    cidade = Column(String, nullable=True)
    estado = Column(String, nullable=True)
    email = Column(String, nullable=True)
    ultima_alteracao = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())


class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipo = Column(Enum(TiposEnum), nullable=False)
    numero = Column(Integer, nullable=False)
    disponivel = Column(Boolean, default=True, nullable=False)
    descricao = Column(String, nullable=True)
    valor = Column(DECIMAL(precision=10, scale=2), nullable=True)
    endereco = Column(String, nullable=True)
    area = Column(Integer, nullable=True)
    ultima_alteracao = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())


class Contrato(Base):
    __tablename__ = "contratos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    data_inicio = Column(Date, nullable=False)
    data_termino = Column(Date, nullable=False)
    valor_aluguel = Column(DECIMAL(precision=10, scale=2), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)
    ultima_alteracao = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())

    inquilino_id = Column(Integer, ForeignKey("inquilinos.id"), nullable=False)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"), nullable=False)
    inquilino = relationship('Inquilino', backref='contratos')
    imovel = relationship('Imovel', backref='contratos')
