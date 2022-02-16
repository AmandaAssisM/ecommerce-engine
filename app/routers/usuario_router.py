from fastapi import APIRouter
import app.services.usuario_services as usuario_services
from app.schemas import usuario_schemas


router = APIRouter()

@router.post('/novo-usuario')
def novo_usuario(usuario: usuario_schemas.UsuarioNovo):
    resultado = usuario_services.novo_usuario(usuario)
    return {'resultado': resultado}

@router.get('/todos-usuarios')
def mostrar_todos_usuarios():
    resultado =usuario_services.pegar_todos_usuarios()
    return {'resultado': resultado}

@router.get('/pegar-usuario-por-id/{id}')
def pegar_usuario_por_id(id: int):
    resultado = usuario_services.pegar_usuario_por_id(id)
    return {'resultado': resultado}

@router.delete('/remover-usuario-por-id/{id}')
def remover_usuario_por_id(id: int):
    resultado = usuario_services.remover_usuario_por_id(id)
    return {'resultado': resultado}

@router.delete('/remover-todos-usuarios')
def remover_todos_usuarios():
    resultado = usuario_services.remover_todos_usuarios()
    return {'resultado': resultado}

@router.put('/editar-usuario/{id}')
def editar_usuario(id: int, usuario_to_edit: usuario_schemas.UsuarioEditar):
    resultado = usuario_services.editar_usuario(id, usuario_to_edit)
    return {'resultado': resultado}
    