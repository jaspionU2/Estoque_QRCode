from sqlalchemy import create_engine, select, update, delete, insert, text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from configs.settings import Config

from model.Model_Equipamento import Equipamento
from model.Model_Carregador import Carregador
from model.Model_Emprestimo import Emprestimo
from model.Model_Carregador import Carregador
from model.Model_Aluno import Aluno
from model.Model_Professor import Professor

from configs.register import engine


class Emprestimo_CRUD:

    async def getAllEmprestimosFromAlunos():
        try:
            with Session(engine) as session:
                query = select("*").select_from(text("getallemprestimosfromalunos"))
                result = session.execute(query).all()
                res = []
                for row in result:
                    emprestimo = Emprestimo(
                        motivo_emprestimo=row[0],
                        data_inicio_emprestimo=row[1],
                        data_fim_emprestimo=row[2],
                        equipamento_emprestimo=0,
                        nome_usuario_emprestimo="",
                    ).__dict__
                    emprestimo.pop("equipamento_emprestimo")
                    emprestimo.pop("nome_usuario_emprestimo")

                    aluno = Aluno(nome=row[3], serie=row[4], turma=row[5]).__dict__

                    equipamento = Equipamento(
                        numero_serie_equipamento=row[6],
                        matricula_equipamento=row[7],
                    ).__dict__
                    equipamento.update({"categoria": row[8]})
                    equipamento.update({"status": row[9]})

                    carregador = Carregador(
                        matricula_carregador=row[10], id_status_carregador=0
                    ).__dict__
                    carregador.pop("id_status_carregador")

                    equipamento.update(dict.fromkeys(["carregador"], carregador))

                    emprestimo.update(dict.fromkeys(["aluno"], aluno))
                    emprestimo.update(dict.fromkeys(["equipamento"], equipamento))

                    res.append(equipamento)
                return res
        except SQLAlchemyError as err:
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            print("Erro inesperado: " + str(err))
            return None

    async def getAllEmprestimosFromProfessores():
        try:
            with Session(engine) as session:
                query = select("*").select_from(
                    text("getallemprestimosfromprofessores")
                )
                result = session.execute(query).all()
                res = []
                for row in result:
                    emprestimo = Emprestimo(
                        motivo_emprestimo=row[0],
                        data_inicio_emprestimo=row[1],
                        data_fim_emprestimo=row[2],
                        equipamento_emprestimo=0,
                        nome_usuario_emprestimo="",
                    ).__dict__
                    emprestimo.pop("equipamento_emprestimo")
                    emprestimo.pop("nome_usuario_emprestimo")

                    professor = Professor(nome=row[3], id_materia=0).__dict__
                    professor.pop("id_materia")
                    professor.update({"materia": row[4]})

                    equipamento = Equipamento(
                        numero_serie_equipamento=row[5],
                        matricula_equipamento=row[6],
                    ).__dict__
                    equipamento.update({"categoria": row[7]})
                    equipamento.update({"status": row[8]})

                    carregador = Carregador(
                        matricula_carregador=row[9], id_status_carregador=0
                    ).__dict__
                    carregador.pop("id_status_carregador")

                    equipamento.update(dict.fromkeys(["carregador"], carregador))

                    emprestimo.update(dict.fromkeys(["professor"], professor))
                    emprestimo.update(dict.fromkeys(["equipamento"], equipamento))

                    res.append(equipamento)
                return res
        except SQLAlchemyError as err:
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            print("Erro inesperado: " + str(err))
            return None

    async def createEmprestimo(new_emprestimo: dict):
        try:
            with Session(engine) as session:
                result = session.execute(insert(Emprestimo).
                                         values(new_emprestimo).
                                         returning(Emprestimo.id, Emprestimo.motivo_emprestimo, Emprestimo.data_inicio_emprestimo, Emprestimo.data_fim_emprestimo, Emprestimo.equipamento_emprestimo, Emprestimo.nome_usuario_emprestimo))
                
                session.commit()
                
                return result.fetchone()._asdict()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False

    async def updateEmprestimo(Id: int, new_value: dict):
        try:
            with Session(engine) as session:
                result = session.execute(update(Emprestimo).
                                         where(Emprestimo.id == Id).
                                         values(new_value).
                                         returning(Emprestimo.id, Emprestimo.motivo_emprestimo, Emprestimo.data_inicio_emprestimo, Emprestimo.data_fim_emprestimo, Emprestimo.equipamento_emprestimo, Emprestimo.nome_usuario_emprestimo))
                
                session.commit()
                
                return result.fetchone()._asdict()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False

    async def deleteEmprestimo(Id: int):
        try:
            with Session(engine) as session:

                result = session.execute(delete(Emprestimo).where(Emprestimo.id == Id))
                session.commit()

                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False
