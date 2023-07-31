from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app import schemas, models
from app.database import get_db

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def obter_inquilinos(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    inquilinos = db.query(models.Inquilino).limit(limit).offset(skip).all()

    return {'results': len(inquilinos), 'inquilinos': inquilinos}


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_inquilino(payload: schemas.Inquilino, db: Session = Depends(get_db)):
    novo_inquilino = models.Inquilino(**payload.model_dump())
    db.add(novo_inquilino)
    db.commit()
    db.refresh(novo_inquilino)

    return {"inquilino": novo_inquilino}

