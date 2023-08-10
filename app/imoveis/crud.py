from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

import imoveis.gateway as gateway
import schemas
from database import get_db

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def obter_imoveis(db: Session = Depends(get_db)):
    imoveis = gateway.obter_imoveis(db=db)

    return {'quantidade': len(imoveis), 'imovels': imoveis}


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_imovel(dados: schemas.Imovel, db: Session = Depends(get_db)):
    return gateway.criar_imovel(dados, db)


@router.get('/{imovel_id}', status_code=status.HTTP_200_OK)
def obter_um_imovel(id: int, db: Session = Depends(get_db)):
    imovel = gateway.obter_um_imovel(id, db)

    return {'imovel': imovel}


@router.patch('/{imovel_id}', status_code=status.HTTP_200_OK)
def editar_um_imovel(id: int, dados: schemas.Imovel, db: Session = Depends(get_db)):
    imovel_atualizado = gateway.editar_um_imovel(id, dados, db)

    return {'imovel_atualizado': imovel_atualizado}


@router.delete('/{imovel_id}', status_code=status.HTTP_204_NO_CONTENT)
def excluir_um_imovel(id: int, db: Session = Depends(get_db)):
    imovel_id = gateway.excluir_um_imovel(id, db)

    return {'message': f'Imóvel {imovel_id} excluído'}
