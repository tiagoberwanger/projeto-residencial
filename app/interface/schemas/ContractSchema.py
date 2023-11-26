from decimal import Decimal
from datetime import date, datetime
from pydantic import BaseModel, Field

from interface.utils.enums import StatusEnum


class ContractPostSchema(BaseModel):
    renter_id: int
    room_id: int
    start_date: date = Field(default='2023-01-01')
    end_date: date = Field(default='2024-01-01')
    rent_value: Decimal = Field(default=Decimal(500))
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)

    class ConfigDict:
        from_attributes = True


class ContractSchema(ContractPostSchema):
    id: int
    last_updated: datetime
