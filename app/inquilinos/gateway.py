from fastapi import status, HTTPException

import models
from utils_db import criar, obter, obter_um, editar, excluir


def criar_inquilino(dados, db):
    return criar(models.Inquilino, dados, db)


def obter_inquilinos(db, pagina: int = 1, limite: int = 10):
    inquilinos = obter(models.Inquilino, page=pagina, limit=limite, db=db)
    return inquilinos


def obter_um_inquilino(inquilino_id, db):
    inquilino = obter_um(models.Inquilino, id=inquilino_id, db=db)

    if not inquilino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Inquilino {inquilino_id} não encontrado')

    return inquilino


def editar_um_inquilino(inquilino_id, dados, db):
    inquilino = obter_um(models.Inquilino, id=inquilino_id, db=db)

    if not inquilino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Inquilino {inquilino_id} não encontrado')

    return editar(models.Inquilino, inquilino_id, payload=dados, db=db)


def excluir_um_inquilino(inquilino_id, db):
    inquilino = obter_um(models.Inquilino, id=inquilino_id, db=db)

    if not inquilino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Inquilino {inquilino_id} não encontrado')

    excluir(models.Inquilino, id=inquilino_id, db=db)
