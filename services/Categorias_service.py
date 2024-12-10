from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Categoria import Categoria

engine = create_engine(Config().DB_URI)


class Categoria_CRUD:

    async def getAllCategorias():

        with Session(engine) as session:

            return session.execute(select(Categoria)).scalars().all()

    async def createCategoria(new_categoria: list[dict]):

        with Session(engine) as session:

            result = session.execute(insert(Categoria).
                                     values(new_categoria))
            session.commit()
            
            return result.rowcount
    
    async def deleteCategoria(Id: int):
        
        with Session(engine) as session:
            
            result = session.execute(delete(Categoria).
                            where(Categoria.id == Id))
            session.commit()
            
            return result       
