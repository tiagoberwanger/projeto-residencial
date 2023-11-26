from typing import List, Optional, Type

from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from data.database import get_db_connection
from data.models.RenterModel import Renter


class RenterRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(self, limit: Optional[int], start: Optional[int]) -> List[Renter]:
        query = self.db.query(Renter)

        return query.offset(start).limit(limit).all()

    def get(self, renter: Renter) -> Type[Renter] | None:
        return self.db.get(Renter, renter.id)

    def create(self, renter: Renter) -> Renter:
        # try:
        self.db.add(renter)
        self.db.commit()
        self.db.refresh(renter)

        # except IntegrityError as e:
        #     self.db.rollback()
        #     raise Exception("Item não pode ser criado por violação de integridade!") from e
        #
        # except Exception as e:
        #     self.db.rollback()
        #     raise Exception("Ocorreu um erro ao criar um item!") from e

        return renter

    def update(self, id: int, renter: Renter) -> Renter:
        renter.id = id
        self.db.merge(renter)
        self.db.commit()
        return renter

    def delete(self, renter: Renter) -> None:
        self.db.delete(renter)
        self.db.commit()
        self.db.flush()
