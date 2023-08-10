from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def obter_contratos(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    contratos = db.query(models.Contrato).limit(limit).offset(skip).all()

    return {'results': len(contratos), 'contratos': contratos}


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_contrato(payload: schemas.Contrato, db: Session = Depends(get_db)):
    novo_contrato = models.Contrato(**payload.model_dump())
    db.add(novo_contrato)
    db.commit()
    db.refresh(novo_contrato)

    return {"contrato": novo_contrato}
