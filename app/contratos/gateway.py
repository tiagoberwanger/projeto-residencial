from fastapi import status, HTTPException

import models
from utils_db import criar, obter, obter_um, editar, excluir


def criar_contrato(dados, db):
    return criar(models.Contrato, dados, db)


def obter_contratos(db, pagina: int = 1, limite: int = 10):
    return obter(models.Contrato, page=pagina, limit=limite, db=db)


def obter_um_contrato(contrato_id, db):
    contrato = obter_um(models.Contrato, id=contrato_id, db=db)

    if not contrato:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contrato {contrato_id} não encontrado')

    return contrato


def editar_um_contrato(contrato_id, dados, db):
    contrato = obter_um(models.Contrato, id=contrato_id, db=db)

    if not contrato:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contrato {contrato_id} não encontrado')

    return editar(models.Contrato, contrato_id, payload=dados, db=db)


def excluir_um_contrato(contrato_id, db):
    contrato = obter_um(models.Contrato, id=contrato_id, db=db)

    if not contrato:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contrato {contrato_id} não encontrado')

    excluir(models.Contrato, id=contrato_id, db=db)
