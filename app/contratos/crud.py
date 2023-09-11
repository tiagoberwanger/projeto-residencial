from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

import contratos.gateway as gateway
import schemas
from database import get_db

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def obter_contratos(db: Session = Depends(get_db)):
    contratos = gateway.obter_contratos(db=db)

    return {'quantidade': len(contratos), 'contratos': contratos}


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_contrato(dados: schemas.Contrato, db: Session = Depends(get_db)):
    return gateway.criar_contrato(dados, db)
