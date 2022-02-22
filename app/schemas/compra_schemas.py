from pydantic import BaseModel


class Compra(BaseModel):
    usuario_id: int
    produto_id: int
