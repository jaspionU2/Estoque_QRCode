from sqlalchemy import select, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, OperationalError, IntegrityError
from model.Model_Materia import Materia
from configs.db_configs import engine
from configs.CustomResponse import CustomResponse
class Materia_CRUD:

    def getAllMaterias() -> CustomResponse | list:
        try:
            with Session(engine) as session:
                return session.execute(select(Materia)).scalars().all()
        except SQLAlchemyError as sql_err:
            session.rollback()
            return CustomResponse(
                type_error=str(sql_err.orig.__class__.__name__),
                sql_message=str(sql_err.orig.diag.message_primary)
            )
        except OperationalError as op_err:
            session.rollback()
            return CustomResponse(
                type_error=str(op_err.orig.__class__.__name__),
                op_message=str(op_err.orig.args[0])
            )
        except IntegrityError as inte_err:
            session.rollback()
            return CustomResponse(
                type_error=str(inte_err.orig.__class__.__name__),
                inte_message=str(inte_err.orig.args[0])
            )
        except Exception as gen_err:
            session.rollback()
            return CustomResponse(
                type_error=str(gen_err.__class__.__name__),
                gen_message=str(gen_err)
            )

    def createMateria(new_materia: dict) -> dict | CustomResponse:
        try:
            with Session(engine) as session:

                result = session.execute(insert(Materia).
                                         values(new_materia).
                                         returning(Materia.id, Materia.materia))
                session.commit()

                return result.fetchone()._asdict()
        except SQLAlchemyError as sql_err:
            session.rollback()
            return CustomResponse(
                value_input=new_materia['materia'],
                type_error=str(sql_err.orig.__class__.__name__),
                sql_message=str(sql_err.orig.diag.message_primary)
            )
        except OperationalError as op_err:
            
            return CustomResponse(
                type_error=str(op_err.orig.__class__.__name__),
                op_message=str(op_err.orig.args[0])
            )
        except IntegrityError as inte_err:
     
            return CustomResponse(
                type_error=str(inte_err.orig.__class__.__name__),
                inte_message=str(inte_err.orig.args[0])
            )
        except Exception as gen_err:
            session.rollback()
            return CustomResponse(
                type_error=str(gen_err.__class__.__name__),
                gen_message=str(gen_err)
            )

    def deleteMateria(Id: int) -> int | CustomResponse :
        try:
            with Session(engine) as session:

                result = session.execute(delete(Materia).
                                         where(Materia.id == Id))
                session.commit()
                
                return result.rowcount
        except SQLAlchemyError as sql_err:
            session.rollback()
            return CustomResponse(
                value_input=Id,
                type_error=str(sql_err.orig.__class__.__name__),
                sql_message=str(sql_err.orig.diag.message_primary)
            )
        except OperationalError as op_err:
            session.rollback()
            return CustomResponse(
                type_error=str(op_err.orig.__class__.__name__),
                op_message=str(op_err.orig.args[0])
            )
        except IntegrityError as inte_err:
            session.rollback()
            return CustomResponse(
                type_error=str(inte_err.orig.__class__.__name__),
                inte_message=str(inte_err.orig.args[0])
            )
        except Exception as gen_err:
            session.rollback()
            return CustomResponse(
                type_error=str(gen_err.__class__.__name__),
                gen_message=str(gen_err)
            )
