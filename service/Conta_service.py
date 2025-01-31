from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from configs.settings import Config
from configs.security import get_password_hash

from model.Model_Conta import Conta

from configs.register import engine


class Conta_CRUD:

    async def doLogin(email: str, senha: str):
        try:
            with Session(engine) as session:
                conta = (
                    session.execute(
                        select(Conta).where(
                            Conta.email_conta == email, Conta.senha_conta == senha
                        )
                    )
                    .scalars()
                    .all()
                )

                if conta is []:
                    return None

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
                contas = session.execute(select(Conta).where(Conta.is_verifed_conta == True)).scalars().all()

                return contas
        except SQLAlchemyError as err:
            print(err._message())
            return None
        except Exception as err:
            print("Erro inesperado: " + str(err))
            return None

    async def getOneConta(email: str) -> Conta:
        try:
            with Session(engine) as session:
                conta = (
                    session.execute(select(Conta).where(Conta.email_conta == email).where(Conta.is_verifed_conta == True))
                    .scalars()
                    .all()
                )

                if conta is []:
                    return None

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

                hashed_passwword = get_password_hash(new_conta["senha_conta"])

                new_conta["senha_conta"] = hashed_passwword
                
                new_conta.update({"is_verifed_conta": False})

                result = session.execute(insert(Conta).
                                         values(new_conta).
                                         returning(Conta.id_conta, Conta.usuario_conta, Conta.email_conta, Conta.senha_conta))

                session.commit()

                return result.fetchone()._asdict()

        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print("Erro inesperado: " + str(err))
            return False
    
    async def turn_verifed_account(email: str):
        try:
            with Session(engine) as session:

                result = session.execute(
                    update(Conta).
                    where(Conta.email_conta == email).
                    values({"is_verifed_conta": True})
                )
                session.commit()

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


    async def updateConta(Id: int, new_value: dict):
        try:
            with Session(engine) as session:

                if "senha_conta" in new_value:
                    new_value["senha_conta"] = get_password_hash(
                        new_value["senha_conta"]
                    )

                result = session.execute(
                    update(Conta).
                    where(Conta.id_conta == Id).
                    values(new_value).
                    returning(Conta.id_conta, Conta.usuario_conta, Conta.email_conta, Conta.senha_conta)
                )
                
                session.commit()

                return result.fetchone()._asdict()
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
                result = session.execute(delete(Conta).where(Conta.id_conta == Id))
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
    
    async def delete_accounts_not_verifed():
        try:
            with Session(engine) as session:
                result = session.execute(delete(Conta).where(Conta.is_verifed_conta == False))
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
