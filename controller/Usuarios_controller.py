from fastapi import APIRouter, Response, status, Depends

from service.Usuarios_service import Aluno_CRUD, Professor_CRUD

from model.Model_Aluno import Aluno
from model.Model_Professor import Professor

from configs import statusMessage
from configs.security import get_current_user

from schema.Schema_Usuario import SchemaAluno, SchemaAlunoPublic
from schema.Schema_Usuario import SchemaProfessor, SchemaProfessorPublic

router_usuario = APIRouter()  

@router_usuario.get('/getAllProfessores')
async def get_Professores(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    professores = await Professor_CRUD.getAllProfessores()

    if professores is None:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return professores

@router_usuario.post('/createProfessor', response_model=SchemaProfessorPublic)
async def create_professor(
    new_professor: SchemaProfessor,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaProfessorPublic:
    if not new_professor or new_professor is []: 
        raise statusMessage.NOT_DATA
        
    result = await Professor_CRUD.createProfessor(new_professor.model_dump())
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_201_CREATED
    
    return result

@router_usuario.put('/updateProfessor/{id}', response_model=SchemaProfessorPublic) 
async def update_Professor(
    id: int,
    new_values: SchemaProfessor,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if not new_values:
        raise statusMessage.NOT_DATA
    
    result = await Professor_CRUD.updateProfessor(id, new_values.model_dump())
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code  = status.HTTP_202_ACCEPTED

@router_usuario.delete('/deleteProfessor/{id}')
async def delete_Professor(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if id <= 0 or id is None:
        raise statusMessage.NOT_DATA
    
    result = await Professor_CRUD.deleteProfessor(id)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED

@router_usuario.get('/getAllAlunos')
async def get_alunos(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    alunos = await Aluno_CRUD.getAllAlunos() 
    
    if alunos is None or alunos is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return alunos

@router_usuario.post('/createAluno', response_model=SchemaAlunoPublic)
async def create_aluno(
    new_aluno: SchemaAluno,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaAlunoPublic:
    if not new_aluno or new_aluno is []:
        raise statusMessage.NOT_DATA
    
    result = await Aluno_CRUD.createAluno(new_aluno.model_dump())
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_201_CREATED
    
    return result

@router_usuario.put('/updateAluno/{id}', response_model=SchemaAlunoPublic) 
async def update_aluno(
    id: int,
    new_values: SchemaAluno,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaAlunoPublic:
    if not new_values:
        raise statusMessage.NOT_DATA
    
    result = await Aluno_CRUD.updateAluno(id, new_values.model_dump())
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code  = status.HTTP_202_ACCEPTED
    
    return result

@router_usuario.delete('/deleteAluno/{id}')
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if id <= 0 or id is None:
        raise statusMessage.NOT_DATA
    
    result = await Aluno_CRUD.deleteAluno(id)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED