from datetime import date, datetime
from pydantic import BaseModel


class Inquilino(BaseModel):
    id: int
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
