from fastapi import FastAPI
from app.routers import usuario_router, produto_router
from app.databases.sqlite_db import create_table

app = FastAPI()
create_table()

app.include_router(usuario_router.router, prefix="/usuario")
app.include_router(produto_router.router, prefix="/produto")