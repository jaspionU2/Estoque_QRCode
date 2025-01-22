from sqlalchemy import create_engine, select, update, delete, insert, text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Atribuicao_permanente import Atribuicao_permanente as Atribuicao
from configs.register import engine

class Atribuicao_CRUD:
    async def getAllAtrubuicoesFromAlunos() -> bool | list:
        try:
            with Session(engine) as session:
                query = select('*').select_from(text('getallatribuicoesfromaluno'))
                result = session.execute(query).all()
                res = []
                for row in result:
                    atribuicao = {
                        "nome_aluno": row[1],
                        "serie_aluno": row[2],
                        "turma_aluno": row[3],
                        "equipamento": {
                            "numero_de_serie": row[4],
                            "matricula": row[5],
                            "categoria": row[6],
                            "status": row[7],
                            "carregador": {
                                "matricula": row[8],
                                "status": row[9]
                            }
                            
                        }
                    }
                    res.append(atribuicao)
                return res
        except SQLAlchemyError as err:
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            print("Erro inesperado: {err}")
            return False
    
    async def getAllAtrubuicoesFromProfessores() -> bool | list:
        try:
            with Session(engine) as session:
                query = select('*').select_from(text('getallatribuicoesfromprofessor'))
                result = session.execute(query).all()
                res = []
                for row in result:
                    atribuicao = {
                        "nome_professor": row[0],
                        "materia": row[1],
                        "equipamento": {
                            "numero_de_serie": row[2],
                            "matricula": row[3],
                            "categoria": row[4],
                            "status": row[5],
                            "carregador": {
                                "matricula": row[6],
                                "status": row[7]
                            }
                            
                        }
                    }
                    res.append(atribuicao)
                return res
        except SQLAlchemyError as err:
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            print("Erro inesperado: {err}")
            return False
    
    async def createAtribuicao(new_atribuicao: dict) -> bool | dict:
        try:
            with Session(engine) as session:
                session.execute(insert(Atribuicao).
                                values(new_atribuicao).
                                returning(Atribuicao.id, Atribuicao.usuario, Atribuicao.equipamento))
                session.commit()
                return True
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
    
    async def updateAtribuicao(Id: int, new_values: dict) -> bool | dict:
        try:
            with Session(engine) as session:
                result = session.execute(update(Atribuicao).
                                where(Atribuicao.id == Id).
                                values(new_values).
                                returning(Atribuicao.id, Atribuicao.usuario, Atribuicao.equipamento))
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
            
    async def deleteAtribuicao(Id: int) -> bool:
        try:
            with Session(engine) as session:
                result = session.execute(delete(Atribuicao).
                                where(Atribuicao.id == Id))
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