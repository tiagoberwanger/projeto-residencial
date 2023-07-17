from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, HTTPException, Response
from .database import get_db

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def obter_inquilinos(
        db: Session = Depends(get_db),
        limit: int = 10,
        page: int = 1
):
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


@router.patch('/{inquilino_id}')
def editar_inquilino(inquilino_id: int, payload: schemas.Inquilino, db: Session = Depends(get_db)):
    filtro_inquilino = db.query(models.Inquilino).filter(models.Inquilino.id == inquilino_id)
    inquilino = filtro_inquilino.first()

    if not inquilino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Inquilino {inquilino_id} não encontrado')
    dados_atualizados = payload.model_dump(exclude_unset=True)
    filtro_inquilino.filter(models.Inquilino.id == inquilino_id).update(dados_atualizados, synchronize_session=False)

    db.commit()
    db.refresh(inquilino)
    return {"inquilino": inquilino}


@router.get('/{inquilino_id}', status_code=status.HTTP_200_OK)
def obter_um_inquilino(inquilino_id: int, db: Session = Depends(get_db)):
    inquilino = db.query(models.Inquilino).filter(models.Inquilino.id == inquilino_id).first()

    if not inquilino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Inquilino {inquilino_id} não encontrado')

    return {"inquilino": inquilino}


@router.delete('/{inquilino_id}', status_code=status.HTTP_204_NO_CONTENT)
def remover_um_inquilino(inquilino_id: int, db: Session = Depends(get_db)):
    filtro_inquilino = db.query(models.Inquilino).filter(models.Inquilino.id == inquilino_id)
    inquilino = filtro_inquilino.first()

    if not inquilino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Inquilino {inquilino_id} não encontrado')

    filtro_inquilino.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
