from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Equipamento import Equipamento

engine = create_engine(Config().DB_URI)

class Equipmanento_CRUD:
    
    async def getAllEquipamentos():
        try:
            with Session(engine) as session:
                return session.execute(select(Equipamento)).scalars().all()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
    async def createEquipamento(new_equipamento: list[Equipamento]):
        try:
            with Session(engine) as session:
                
                equipamentos = [equipamento_data.__dict__ for equipamento_data in new_equipamento]
                
                for equipamento in equipamentos:
                    equipamento.pop("_sa_instance_state", None)
                
                result = session.execute(insert(Equipamento).
                                        values(equipamentos))
                session.commit()
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
        
    async def updateEquipamento(Id: int, new_value: Equipamento):
        try:
            with Session(engine) as session:
                
                new_data = new_value.__dict__
                new_data.pop("_sa_instance_state", None)
                
                result = session.execute(update(Equipamento).
                                        where(Equipamento.id == Id).
                                        values(new_data))
                session.commit()
                
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
            
    async def deleteEquipamento(Id: int):
        try:
            with Session(engine) as session:
                
                result = session.execute(delete(Equipamento).
                                        where(Equipamento.id == Id))
                session.commit()
                
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
    

