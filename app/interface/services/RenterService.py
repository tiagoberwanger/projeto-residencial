from typing import List, Optional, Type

from fastapi import Depends
from data.models.RenterModel import Renter

from data.repositories.RenterRepository import RenterRepository
from interface.schemas.RenterSchema import  RenterPostSchema


class RenterService:
    renter_repository: RenterRepository

    def __init__(self, renter_repository: RenterRepository = Depends()) -> None:
        self.renter_repository = renter_repository

    def list(
            self,
            pageSize: Optional[int] = 100,
            startIndex: Optional[int] = 0,
    ) -> List[Renter]:
        return self.renter_repository.list(pageSize, startIndex)

    def get(self, renter_id: int) -> Type[Renter] | None:
        return self.renter_repository.get(Renter(id=renter_id))

    def create(self, body: RenterPostSchema) -> Renter:
        return self.renter_repository.create(
            Renter(
                name=body.name,
                cpf=body.cpf,
                birth_date=body.birth_date,
                city=body.city,
                state=body.state,
                email=body.email
            )
        )

    def update(self, renter_id: int, body: RenterPostSchema) -> Renter:
        return self.renter_repository.update(
            renter_id,
            Renter(
                name=body.name,
                cpf=body.cpf,
                birth_date=body.birth_date,
                city=body.city,
                state=body.state,
                email=body.email
            )
        )

    def delete(self, renter_id: int) -> None:
        return self.renter_repository.delete(Renter(id=renter_id))