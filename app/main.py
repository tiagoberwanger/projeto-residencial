from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models, inquilinos, imoveis, contratos
from .contratos import crud
from .database import engine
from .imoveis import crud
from .inquilinos import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(inquilinos.crud.router, tags=['Inquilinos'], prefix='/api/inquilinos')
app.include_router(imoveis.crud.router, tags=['Imoveis'], prefix='/api/imoveis')
app.include_router(contratos.crud.router, tags=['Contratos'], prefix='/api/contratos')
