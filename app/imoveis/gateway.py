from fastapi import status, HTTPException

import models
from utils_db import criar, obter, obter_um, editar, excluir


def criar_imovel(dados, db):
    return criar(models.Imovel, dados, db)


def obter_imoveis(db, pagina: int = 1, limite: int = 10):
    imovels = obter(models.Imovel, page=pagina, limit=limite, db=db)
    return imovels


def obter_um_imovel(imovel_id, db):
    imovel = obter_um(models.Imovel, id=imovel_id, db=db)

    if not imovel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Imóvel {imovel_id} não encontrado')

    return imovel


def editar_um_imovel(imovel_id, dados, db):
    imovel = obter_um(models.Imovel, id=imovel_id, db=db)

    if not imovel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Imóvel {imovel_id} não encontrado')

    return editar(models.Imovel, imovel_id, payload=dados, db=db)


def excluir_um_imovel(imovel_id, db):
    imovel = obter_um(models.Imovel, id=imovel_id, db=db)

    if not imovel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Imóvel {imovel_id} não encontrado')

    excluir(models.Imovel, id=imovel_id, db=db)
