import app.repository.produto_repository as produto_repository


def cadastrar_novo_produto(produto):
    result = produto_repository.cadastrar_novo_produto(produto)
    return result

def pegar_todos_os_produtos():
    result = produto_repository.pegar_todos()
    return result

def remover_produto_por_id(id):
    result = produto_repository.remover_pelo_id(id)
    return result

def remover_todos_produtos():
    result = produto_repository.remover_todos()
    return result