from fastapi import APIRouter
import app.services.produto_services as produto_services
from app.schemas import produto_schemas


router = APIRouter()

@router.post('/novo-produto')
def novo_produto(produto: produto_schemas.ProdutoNovo):
    resultado = produto_services.cadastrar_novo_produto(produto)
    return {'resultado': resultado}

@router.get('/mostrar-todos-os-produtos')
def mostrar_todos_os_produtos():
    resultado = produto_services.pegar_todos_os_produtos()
    return {'resultado': resultado}

@router.get('/mostrar-produto-por-id/{id}')
def mostrar_produto_por_id(id: int):
    resultado = produto_services.pegar_produto_por_id(id)
    return {'resultado': resultado}

@router.delete('/remover-produto-por-id/{id}')
def remover_produto_por_id(id: int):
    resultado = produto_services.remover_produto_por_id(id)
    return {'resultado': resultado}

@router.delete('/remover-todos-produtos')
def remover_todos_produtos():
    resultado = produto_services.remover_todos_produtos()
    return {'resultado': resultado}

@router.put('/editar-produto/{id}')
def editar_produto(id: int, produto_to_edit: produto_schemas.ProdutoEditar):
    resultado = produto_services.editar_produto(id, produto_to_edit)
    return {'resultado': resultado}
