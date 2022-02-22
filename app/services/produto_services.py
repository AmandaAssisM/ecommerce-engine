import app.repository.produto_repository as produto_repository
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


def cadastrar_novo_produto(produto):
    result = produto_repository.cadastrar_novo_produto(produto)
    return result

def pegar_todos_os_produtos():
    result = produto_repository.pegar_todos()
    return result

def pegar_produto_por_id(id):
    produto = produto_repository.pegar_produto_por_id(id)
    if not produto:
        raise HTTPException(400, "Produto não encontrado")
    return produto

def remover_produto_por_id(id):
    result = produto_repository.remover_pelo_id(id)
    return result

def remover_todos_produtos():
    result = produto_repository.remover_todos()
    return result

def editar_produto(id, produto_to_edit):
    produto_to_edit_dict = jsonable_encoder(produto_to_edit)
    result = produto_repository.editar(id, produto_to_edit_dict)
    return result
    