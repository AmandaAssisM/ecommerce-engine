from fastapi import HTTPException
from sqlalchemy.ext.serializer import dumps
import app.repository.usuario_repository as usuario_repository
import app.services.produto_services as produto_services
from fastapi.encoders  import jsonable_encoder


def novo_usuario(usuario):
    result = usuario_repository.criar_usuario(usuario)
    return result

def pegar_todos_usuarios():
    result = usuario_repository.pegar_todos()
    return result

def pegar_usuario_por_id(id):
    usuario = usuario_repository.pegar_pelo_id(id)
    if not usuario:
        raise HTTPException(400, "Usuário não encontrado")
    return usuario

def remover_usuario_por_id(id):
    result = usuario_repository.remover_pelo_id(id)
    return result

def remover_todos_usuarios():
    result = usuario_repository.remover_todos()
    return result

def editar_usuario(id, usuario_to_edit):
    usuario_to_edit_dict = jsonable_encoder(usuario_to_edit)
    result = usuario_repository.editar(id, usuario_to_edit_dict)
    return result

def efetuar_compra(compra_info):
    produto = produto_services.pegar_produto_por_id(compra_info.produto_id)
    if not produto.estoque:
        raise HTTPException(400, "Produto sem estoque")
    
    usuario = pegar_usuario_por_id(compra_info.usuario_id)
    if usuario.saldo < produto.valor:
        raise HTTPException(400, "Saldo insuficiente!")

    produto.estoque = produto.estoque - 1
    usuario.saldo = usuario.saldo - produto.valor
    editar_usuario(usuario.id, usuario)
    produto_services.editar_produto(produto.id, produto)
    
    return "compra efetuada"
