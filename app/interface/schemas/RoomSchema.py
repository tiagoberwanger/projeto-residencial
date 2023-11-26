from decimal import Decimal

from datetime import datetime
from pydantic import BaseModel, Field

from interface.utils.enums import RoomEnum


class RoomPostSchema(BaseModel):
    room_type: RoomEnum = Field(default=RoomEnum.STUDIO)
    room_number: int = Field(gt=0, lt=6, default=1)
    is_available: bool = Field(default=True)
    description: str | None = Field(default="Quitinete de 35m²")
    value: Decimal | None = Field(default=Decimal(500))
    address: str | None = Field(default="Rua 25 de julho, 551")

    class ConfigDict:
        from_attributes = True


class RoomSchema(RoomPostSchema):
    id: int
    last_updated: datetime
