from typing import List, Optional, Type

from fastapi import Depends
from sqlalchemy.orm import Session

from data.database import get_db_connection
from data.models.ContractModel import Contract


class ContractRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(self, limit: Optional[int], start: Optional[int]) -> List[Contract]:
        query = self.db.query(Contract)

        return query.offset(start).limit(limit).all()

    def get(self, contract: Contract) -> Type[Contract] | None:
        return self.db.get(Contract, contract.id)

    def create(self, contract: Contract) -> Contract:
        self.db.add(contract)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def update(self, id: int, contract: Contract) -> Contract:
        contract.id = id
        self.db.merge(contract)
        self.db.commit()
        return contract

    def delete(self, contract: Contract) -> None:
        self.db.delete(contract)
        self.db.commit()
        self.db.flush()
