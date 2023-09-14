from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

import contratos.gateway as gateway
import inquilinos.gateway as inquilino_gateway
import imoveis.gateway as imovel_gateway
import schemas
from database import get_db

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def obter_contratos(db: Session = Depends(get_db)):
    contratos = gateway.obter_contratos(db=db)

    return {'quantidade': len(contratos), 'contratos': contratos}


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_contrato(contrato: schemas.Contrato, db: Session = Depends(get_db)):
    inquilino = inquilino_gateway.obter_um_inquilino(contrato.inquilino_id, db)
    if not inquilino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inquilino não encontrado")

    imovel = imovel_gateway.obter_um_imovel(contrato.imovel_id, db)
    if not imovel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Imóvel não encontrado")

    return gateway.criar_contrato(contrato, db)
