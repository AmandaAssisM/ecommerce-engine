import app.repository.usuario_repository as usuario_repository


def novo_usuario(usuario):
    result = usuario_repository.criar_usuario(usuario)
    return result

def pegar_todos_usuarios():
    result = usuario_repository.pegar_todos()
    return result

def pegar_usuario_por_id(id):
    result = usuario_repository.pegar_pelo_id(id)
    return result

def remover_usuario_por_id(id):
    result = usuario_repository.remover_pelo_id(id)
    return result

def remover_todos_usuarios():
    result = usuario_repository.remover_todos()
    return result

def editar_usuario(id, usuario_to_edit):
    result = usuario_repository.editar(id, usuario_to_edit)
    return result
