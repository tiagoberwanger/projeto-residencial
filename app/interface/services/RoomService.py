from typing import List, Optional, Type

from fastapi import Depends
from data.models.RoomModel import Room

from data.repositories.RoomRepository import RoomRepository
from interface.schemas.RoomSchema import RoomPostSchema


class RoomService:
    room_repository: RoomRepository

    def __init__(self, room_repository: RoomRepository = Depends()) -> None:
        self.room_repository = room_repository

    def list(
            self,
            pageSize: Optional[int] = 100,
            startIndex: Optional[int] = 0,
    ) -> List[Room]:
        return self.room_repository.list(pageSize, startIndex)

    def get(self, room_id: int) -> Type[Room] | None:
        return self.room_repository.get(Room(id=room_id))

    def create(self, body: RoomPostSchema) -> Room:
        return self.room_repository.create(
            Room(
                room_type=body.room_type,
                room_number=body.room_number,
                is_available=body.is_available,
                description=body.description,
                value=body.value,
                address=body.address
            )
        )

    def update(self, room_id: int, body: RoomPostSchema) -> Room:
        return self.room_repository.update(
            room_id,
            Room(
                room_type=body.room_type,
                room_number=body.room_number,
                is_available=body.is_available,
                description=body.description,
                value=body.value,
                address=body.address
            )
        )

    def delete(self, room_id: int) -> None:
        return self.room_repository.delete(Room(id=room_id))