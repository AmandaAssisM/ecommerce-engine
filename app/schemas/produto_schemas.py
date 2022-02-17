from pydantic import BaseModel


class ProdutoNovo(BaseModel):
    nome: str
    estoque: int
    categoria: str
    valor: float

