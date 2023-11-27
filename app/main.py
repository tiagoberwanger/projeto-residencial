from fastapi import FastAPI

from data.models.BaseModel import init

# Core Application Instance
from interface.routers.v1.RenterRouter import RenterRouter
from interface.routers.v1.RoomRouter import RoomRouter
from interface.routers.v1.ContractRouter import ContractRouter

Tags = [
    {
        "name": "contract",
        "description": "Contains CRUD operation on Contracts",
    },
    {
        "name": "renter",
        "description": "Contains CRUD operation on Renters",
    },
    {
        "name": "room",
        "description": "Contains CRUD operation on Rooms",
    },
]

app = FastAPI(openapi_tags=Tags)

# Add Routers
app.include_router(RenterRouter)
app.include_router(RoomRouter)
app.include_router(ContractRouter)

# Initialise Data Model Attributes
init()
