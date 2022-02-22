from app.databases.sqlite_db import get_db
from app.models.produto_model import Produto


def cadastrar_novo_produto(produto):
    db = get_db()
    produto_db = Produto(**produto.dict())
    db.add(produto_db)
    db.commit()
    db.refresh(produto_db)
    db.close()
    return produto_db

def pegar_todos():
    db = get_db()
    produtos = db.query(Produto).all()
    db.close()
    return produtos

def pegar_produto_por_id(id):
    db = get_db()
    produto = db.query(Produto).get(id)
    db.close()
    return produto

def remover_pelo_id(id):
    db = get_db()
    resultado = db.query(Produto).filter_by(id=id).delete()
    db.commit()
    db.close()
    return resultado

def remover_todos():
    db = get_db()
    resultado = db.query(Produto).delete()
    db.commit()
    db.close()
    return resultado

def editar(id, produto_to_edit):
    db = get_db()
    produto = db.query(Produto).filter(Produto.id == id).update(produto_to_edit)
    db.commit()
    db.close()
    return produto
