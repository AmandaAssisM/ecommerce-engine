from pydantic import BaseModel


class UsuarioNovo(BaseModel): 
    nome: str
    email: str
    cpf: str
    saldo: float


class UsuarioEditar(BaseModel):
    nome: str
    email: str
    cpf: str
    saldo: float
