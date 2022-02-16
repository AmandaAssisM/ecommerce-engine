from app.databases.sqlite_db import get_db
from app.models.usuario_model import Usuario
from fastapi.encoders import jsonable_encoder


def criar_usuario(usuario):
    db = get_db()
    usuario_db = Usuario(**usuario.dict())
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    db.close()
    return usuario_db

def pegar_todos():
    db = get_db()
    usuarios = db.query(Usuario).all()
    db.close()
    return usuarios

def pegar_pelo_id(id):
    db = get_db()
    usuario = db.query(Usuario).get(id)
    db.close()
    return usuario

def remover_pelo_id(id):
    db = get_db()
    resultado = db.query(Usuario).filter_by(id=id).delete()
    db.commit()
    db.close()
    return resultado

def remover_todos():
    db = get_db()
    resultaddo = db.query(Usuario).delete()
    db.commit()
    db.close()
    return resultaddo

def editar(id, usuario_to_edit):
    db = get_db()
    usuario = db.query(Usuario).get(id)

    usuario_db = jsonable_encoder(usuario)
    usuario_to_edit_data = usuario_to_edit.dict()
    for campo in usuario_db:
        if campo in usuario_to_edit_data.keys():
            setattr(usuario, campo, usuario_to_edit_data[campo])

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    db.close()
    return usuario
