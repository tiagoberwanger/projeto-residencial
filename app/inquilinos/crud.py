from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

import inquilinos.gateway as gateway
import schemas
from database import get_db

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def obter_inquilinos(db: Session = Depends(get_db)):
    inquilinos = gateway.obter_inquilinos(db=db)

    return {'quantidade': len(inquilinos), 'inquilinos': inquilinos}


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_inquilino(dados: schemas.Inquilino, db: Session = Depends(get_db)):
    return gateway.criar_inquilino(dados, db)


@router.get('/{inquilino_id}', status_code=status.HTTP_200_OK)
def obter_um_inquilino(id: int, db: Session = Depends(get_db)):
    inquilino = gateway.obter_um_inquilino(id, db)

    return {'inquilino': inquilino}


@router.patch('/{inquilino_id}', status_code=status.HTTP_200_OK)
def editar_um_inquilino(id: int, dados: schemas.Inquilino, db: Session = Depends(get_db)):
    inquilino_atualizado = gateway.editar_um_inquilino(id, dados, db)

    return {'inquilino_atualizado': inquilino_atualizado}


@router.delete('/{inquilino_id}', status_code=status.HTTP_204_NO_CONTENT)
def excluir_um_inquilino(id: int, db: Session = Depends(get_db)):
    inquilino_id = gateway.excluir_um_inquilino(id, db)

    return {'message': f'Inquilino {inquilino_id} excluído'}
