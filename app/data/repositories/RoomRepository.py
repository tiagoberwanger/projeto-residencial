from typing import List, Optional, Type

from fastapi import Depends
from sqlalchemy.orm import Session

from data.database import get_db_connection
from data.models.RoomModel import Room


class RoomRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(self, limit: Optional[int], start: Optional[int]) -> List[Room]:
        query = self.db.query(Room)

        return query.offset(start).limit(limit).all()

    def get(self,  room: Room) -> Type[Room] | None:
        return self.db.get(Room, room.id)

    def create(self, room: Room) -> Room:
        self.db.add(room)
        self.db.commit()
        self.db.refresh(room)
        return room

    def update(self, id: int, room: Room) -> Room:
        room.id = id
        self.db.merge(room)
        self.db.commit()
        return room

    def delete(self, room: Room) -> None:
        self.db.delete(room)
        self.db.commit()
        self.db.flush()
