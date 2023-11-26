from typing import List, Optional

from fastapi import APIRouter, Depends
from starlette import status

from interface.schemas.ContractSchema import ContractSchema, ContractPostSchema
from interface.services.ContractService import ContractService

ContractRouter = APIRouter(prefix="/v1/contracts", tags=["contract"])


@ContractRouter.get("/", response_model=List[ContractSchema])
def index(
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
        contractService: ContractService = Depends(),
):
    return [
        contract
        for contract in contractService.list(
            pageSize, startIndex
        )
    ]


@ContractRouter.post("/", response_model=ContractSchema, status_code=status.HTTP_201_CREATED)
def create(contract: ContractPostSchema, contractService: ContractService = Depends()):
    return contractService.create(contract)
