# from sqlalchemy import create_engine, select, String, insert, update, delete
# from sqlalchemy.orm import Session, registry, Mapped, mapped_column

# from model.Model_Aluno import Aluno, Serie, Turma
# from model.Model_Carregador import Carregador

# def selectDB():

#     engine = create_engine('postgresql+psycopg2://postgres:220206@localhost/estoquemirim')

#     session = Session(engine)
    
#     aluno = Carregador

#     alunos = select(aluno)

#     for aluno in session.scalars(alunos):
#         print(aluno)
        
# def insertDB():
#     engine = create_engine('postgresql+psycopg2://postgres:220206@localhost/estoquemirim')
    
#     stmt = insert(Carregador).values(matricula_carregador='C0001', id_status='1') 
    
    
#     with engine.connect() as conn:
#         result = conn.execute(stmt)
#         conn.commit()

