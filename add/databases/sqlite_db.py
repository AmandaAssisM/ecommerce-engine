from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = "sqlite:///./app/meu_db.db"
engine = create_engine(database_url)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def create_table():
    Base.metadata.create_all(engine)

def get_db():
    db = Session()
    return db