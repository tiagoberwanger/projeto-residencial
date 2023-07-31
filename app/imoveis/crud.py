from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def obter_imoveis(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    imoveis = db.query(models.Imovel).limit(limit).offset(skip).all()

    return {'results': len(imoveis), 'imoveis': imoveis}


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_imovel(payload: schemas.Imovel, db: Session = Depends(get_db)):
    novo_imovel = models.Imovel(**payload.model_dump())
    db.add(novo_imovel)
    db.commit()
    db.refresh(novo_imovel)

    return {"imovel": novo_imovel}
