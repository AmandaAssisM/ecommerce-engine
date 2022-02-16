from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from app.databases.sqlite_db import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    saldo = Column(Float, nullable=False)

