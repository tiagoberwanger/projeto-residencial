from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from database import engine
from models import Base
from inquilinos import crud as inquilinos_crud
from contratos import crud as contratos_crud
from imoveis import crud as imoveis_crud


Base.metadata.create_all(bind=engine)

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

app.include_router(inquilinos_crud.router, tags=['Inquilinos'], prefix='/api/inquilinos')
app.include_router(imoveis_crud.router, tags=['Imoveis'], prefix='/api/imoveis')
app.include_router(contratos_crud.router, tags=['Contratos'], prefix='/api/contratos')
