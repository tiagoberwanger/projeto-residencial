from enum import Enum
from datetime import date, datetime
from pydantic import BaseModel


class Inquilino(BaseModel):
    nome: str
    cpf: int
    data_nascimento: date | None = None
    cidade: str | None = None
    estado: str | None = None
    email: str | None = None
    ultima_alteracao: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class TiposEnum(str, Enum):
    QUARTO = 'quarto'
    QUITINETE = 'quitinete'
    APARTAMENTO = 'apartamento'


class Imovel(BaseModel):
    tipo: TiposEnum
    numero: int
    disponivel: bool
    descricao: str | None = None
    valor: int | None = None
    endereco: str | None = None
    area: int | None = None
    ultima_alteracao: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class StatusEnum(Enum):
    ATIVO = 'ativo'
    FINALIZADO = 'finalizado'
    RENOVADO = 'renovado'


class Contrato(BaseModel):
    inquilino_id: int
    imovel_id: int
    data_inicio: datetime
    data_termino: datetime
    valor_aluguel: int
    status: StatusEnum
    ultima_alteracao: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
