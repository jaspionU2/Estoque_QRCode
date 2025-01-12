from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from configs.settings import Config
from configs.security import get_password_hash

from model.Model_Conta import Conta

engine = create_engine(Config().DB_URI)

class Conta_CRUD:
    
    async def doLogin(email: str, senha: str):
        try:
            with Session(engine) as session:
                conta = session.execute(select(Conta).where(Conta.email_conta == email, Conta.senha_conta == senha)).scalars().all()
                
                if conta is []: return None
                
                return conta[0]
        except SQLAlchemyError as err:
            print(err._message())
            return None
        except Exception as err:
            print("Erro inesperado: {err}")
            return None
        
    async def getAllConta():
        try:
            with Session(engine) as session:
                contas = session.execute(select(Conta)).scalars().all()
                
                return contas
        except SQLAlchemyError as err:
            print(err._message())
            return None
        except Exception as err:
            print("Erro inesperado: {err}")
            return None
        
    async def getOneConta(email: str) -> Conta:
        try:
            with Session(engine) as session:
                conta = session.execute(select(Conta).where(Conta.email_conta == email)).scalars().all()
                
                if conta is []:  return None

                conta = conta[0].__dict__
                
                conta.pop("_sa_instance_state")
                
                return conta
        except SQLAlchemyError as err:
            print(err._message())
            return None
        except Exception as err:
            print("Erro inesperado: " + str(err))
            return None
    
    async def createConta(new_conta: dict):
        try:
            with Session(engine) as session:
                new_conta["senha_conta"] = get_password_hash(new_conta["senha_conta"])
                
                session.execute(insert(Conta).values(new_conta))
                
                session.commit()
                
                return session.execute(select(Conta).where(Conta.email_conta == new_conta['email_conta'])).scalars().all()
                
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: " + str(err))
            return None
        
    async def updateConta(Id: int, new_value: dict):
        try:
            with Session(engine) as session:
                new_value["senha_conta"] = get_password_hash(new_value["senha_conta"]) if not new_value["senha_conta"] is "" else new_value["senha_conta"]
                
                result = session.execute(update(Conta).
                                        where(Conta.id_conta == Id).
                                        values(new_value))
                session.commit()
                
                print(new_value)
                
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print("Erro inesperado: " + str(err))
            return False
    
    async def deleteConta(Id: int):
        try:
            with Session(engine) as session:
                result = session.execute(delete(Conta).
                                        where(Conta.id == Id))
                session.commit()
                
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False