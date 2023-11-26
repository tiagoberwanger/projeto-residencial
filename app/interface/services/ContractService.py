from typing import List, Optional, Type

from fastapi import Depends

from data.models.ContractModel import Contract
from data.repositories.ContractRepository import ContractRepository
from interface.schemas.ContractSchema import ContractPostSchema


class ContractService:
    contract_repository: ContractRepository

    def __init__(self, contract_repository: ContractRepository = Depends()) -> None:
        self.contract_repository = contract_repository

    def list(
            self,
            pageSize: Optional[int] = 100,
            startIndex: Optional[int] = 0,
    ) -> List[Contract]:
        return self.contract_repository.list(pageSize, startIndex)

    def get(self, contract_id: int) -> Type[Contract] | None:
        return self.contract_repository.get(Contract(id=contract_id))

    def create(self, body: ContractPostSchema) -> Contract:
        return self.contract_repository.create(
            Contract(
                renter_id=body.renter_id,
                room_id=body.room_id,
                start_date=body.start_date,
                end_date=body.end_date,
                rent_value=body.rent_value,
                status=body.status
            )
        )

    def update(self, contract_id: int, body: ContractPostSchema) -> Contract:
        return self.contract_repository.update(
            contract_id,
            Contract(
                renter_id=body.renter_id,
                room_id=body.room_id,
                start_date=body.start_date,
                end_date=body.end_date,
                rent_value=body.rent_value,
                status=body.status
            )
        )

    def delete(self, contract_id: int) -> None:
        return self.contract_repository.delete(Contract(id=contract_id))