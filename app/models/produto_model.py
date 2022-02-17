from sqlalchemy  import Column, Float, String, Integer, Float
from sqlalchemy.orm import relationship
from app.databases.sqlite_db import Base


class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    estoque = Column(Integer, nullable=False)
    categoria = Column(String, nullable=False)
    valor = Column(Float, nullable=False)

