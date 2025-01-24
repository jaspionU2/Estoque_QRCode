from sqlalchemy import  select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from model.Model_Equipamento import Equipamento
from model.Model_Carregador import Carregador
from model.Model_Categoria import Categoria
from model.Model_Status import Status
from sqlalchemy.orm import aliased

from configs.register import engine

class Equipamento_CRUD:

    def getAllEquipamentos() -> list:
        try:
            with Session(engine) as session:
                categoria_alias = aliased(Categoria)
                status_alias = aliased(Status)
                carregador_alias = aliased(Carregador)
                
                query = (
                    select(
                        Equipamento.numero_serie_equipamento,
                        Equipamento.matricula_equipamento,
                        categoria_alias.categoria.label("categoria_equipamento"),
                        status_alias.status.label("status_equipamento"),
                        carregador_alias.matricula_carregador,
                        carregador_alias.id_status_carregador.label("status_carregador"),
                    )
                    .join(categoria_alias, Equipamento.id_categoria_equipamento == categoria_alias.id, isouter=True)
                    .join(status_alias, Equipamento.id_status_equipamento == status_alias.id, isouter=True)
                    .join(carregador_alias, Equipamento.id_equipamento == carregador_alias.id_carregador, isouter=True)
                )
                
                result = session.execute(query).fetchall()

                res = []
                for row in result:
                    equi = {
                        "numero_serie_equipamento": row.numero_serie_equipamento,
                        "matricula_equipamento": row.matricula_equipamento,
                        "categoria_equipamento": row.categoria_equipamento,
                        "status_equipamento": row.status_equipamento,
                        "carregador": {
                            "matricula_carregador": row.matricula_carregador,
                            "status_carregador": row.status_carregador,
                        },
                    }
                    res.append(equi)
                return res
        except SQLAlchemyError as err:
            print(f"Erro no SQLAlchemy: {str(err)}")
            return []
        except Exception as err:
            print(f"Erro inesperado: {str(err)}")
            return []

    def createEquipamento(new_equipamento: dict) -> bool | dict:
            try:
                with Session(engine) as session:
                    result = session.execute(insert(Equipamento).
                                            values(new_equipamento).
                                            returning(
                                                Equipamento.id_equipamento, Equipamento.numero_serie_equipamento, Equipamento.matricula_equipamento, Equipamento.id_categoria_equipamento, Equipamento.id_status_equipamento
                                            ))
                    
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

    def updateEquipamento(Id: int, new_equipamento: dict) -> bool | dict:
        try:
            with Session(engine) as session:

                result = session.execute(
                    update(Equipamento).where(Equipamento.id_equipamento == Id).
                                        values(new_equipamento).
                                        returning(  
                                            Equipamento.id_equipamento, Equipamento.numero_serie_equipamento, Equipamento.matricula_equipamento, Equipamento.id_categoria_equipamento, Equipamento.id_status_equipamento 
                                        ))
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

    def deleteEquipamento(Id: int) -> bool:
        try:
            with Session(engine) as session:

                result = session.execute(
                    delete(Equipamento).where(Equipamento.id == Id)
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
            print(f"Erro inesperado: {err}")
            return False
