from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette import status

from interface.schemas.RoomSchema import RoomSchema, RoomPostSchema
from interface.services.RoomService import RoomService

RoomRouter = APIRouter(prefix="/v1/rooms", tags=["room"])


@RoomRouter.get("/", response_model=List[RoomSchema])
def index(
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
        roomService: RoomService = Depends(),
):
    return [
        room
        for room in roomService.list(
            pageSize, startIndex
        )
    ]


@RoomRouter.post("/", response_model=RoomSchema, status_code=status.HTTP_201_CREATED)
def create(room: RoomPostSchema, roomService: RoomService = Depends()):
    return roomService.create(room)
