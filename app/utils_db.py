from sqlalchemy.exc import IntegrityError, MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound


def criar(model, payload, db):
    try:
        novo_item = model(**payload.model_dump())
        db.add(novo_item)
        db.commit()
        db.refresh(novo_item)
        return novo_item

    except IntegrityError as e:
        db.rollback()
        raise Exception("Item não pode ser criado por violação de integridade!") from e

    except Exception as e:
        db.rollback()
        raise Exception("Ocorreu um erro ao criar um item!") from e


def obter(model, page, limit, db):
    try:
        skip = (page - 1) * limit
        itens = db.query(model).limit(limit).offset(skip).all()
        return itens

    except Exception as e:
        raise Exception("Ocorreu um erro ao obter itens!") from e


def obter_um(model, id, db):
    try:
        item = db.query(model).filter(model.id == id)
        if item.count() > 1:
            raise MultipleResultsFound("Múltiplos itens encontrados!")
        if item is None:
            raise NoResultFound("Item não encontrado!")
        return item.first()
    except Exception as e:
        raise Exception("Ocorreu um erro ao obter um item!") from e


def editar(model, id, payload, db):
    try:
        item_para_atualizar = db.query(model).filter(model.id == id)
        item = item_para_atualizar.first()
        if item is None:
            raise NoResultFound("Item não encontrado!")

        dados_atualizados = payload.model_dump(exclude_unset=True)
        item_para_atualizar.filter(model.id == id).update(dados_atualizados, synchronize_session=False)

        db.commit()
        db.refresh(item)

        return item
    except Exception as e:
        db.rollback()
        raise Exception("Ocorreu um erro ao editar um item!") from e


def excluir(model, id, db):
    try:
        item_para_remover = db.query(model).filter(model.id == id)
        if item_para_remover is None:
            raise NoResultFound("Item não encontrado!")
        item_para_remover.delete(synchronize_session=False)
        db.commit()

    except Exception as e:
        db.rollback()
        raise Exception("Ocorreu um erro ao excluir um item!") from e
