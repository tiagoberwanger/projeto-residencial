def criar(model, payload, db):
    novo_item = model(**payload.model_dump())

    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)

    return novo_item


def obter(model, page, limit, db):
    skip = (page - 1) * limit
    itens = db.query(model).limit(limit).offset(skip).all()

    return itens


def obter_um(model, id, db):
    item = db.query(model).filter(model.id == id).first()

    return item


def editar(model, id, payload, db):
    item_para_atualizar = db.query(model).filter(model.id == id)
    item = item_para_atualizar.first()
    dados_atualizados = payload.model_dump(exclude_unset=True)
    item_para_atualizar.filter(model.id == id).update(dados_atualizados, synchronize_session=False)

    db.commit()
    db.refresh(item)

    return item


def excluir(model, id, db):
    item_para_remover = db.query(model).filter(model.id == id)
    item_para_remover.delete(synchronize_session=False)

    db.commit()

    return item_para_remover
