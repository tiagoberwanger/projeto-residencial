from typing import List, Optional

from fastapi import APIRouter, Depends
from starlette import status

from interface.schemas.RenterSchema import RenterSchema, RenterPostSchema
from interface.services.RenterService import RenterService

RenterRouter = APIRouter(prefix="/v1/renters", tags=["renter"])

@RenterRouter.get("/", response_model=List[RenterSchema])
def index(
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    renterService: RenterService = Depends(),
):
    return [
        renter
        for renter in renterService.list(
            pageSize, startIndex
        )
    ]


@RenterRouter.post("/", response_model=RenterSchema, status_code=status.HTTP_201_CREATED)
def create(renter: RenterPostSchema, renterService: RenterService = Depends()):
    return renterService.create(renter)
