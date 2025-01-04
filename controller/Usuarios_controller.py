from fastapi import APIRouter, Response, status
from services.Usuarios_service import Aluno_CRUD, Professor_CRUD
from model.Model_Aluno import Aluno
from model.Model_Professor import Professor

from configs.statusMessage import messages

router_usuario = APIRouter()  

@router_usuario.get('/getAllProfessores')
async def get_Professores(res: Response) -> list[dict]:
    professores = await Professor_CRUD.getAllProfessores()

    if professores is None:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return professores

@router_usuario.post('/createProfessor')
async def create_professor(new_professor: list[Professor], res: Response) -> dict:
    if not new_professor or new_professor is []: 
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
        
    result = await Professor_CRUD.createProfessor(new_professor)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]

@router_usuario.put('/updateProfessor/{id}') 
async def update_Professor(id: int, new_values: dict, res: Response) -> dict:
    if not new_values:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Professor_CRUD.updateProfessor(id, new_values)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code  = status.HTTP_200_OK
    return messages["sucess"]

@router_usuario.delete('/deleteProfessor/{id}')
async def delete_Professor(id: int, res: Response) -> dict:
    if id <= 0 or id is None:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Professor_CRUD.deleteProfessor(id)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]

@router_usuario.get('/getAllAlunos')
async def get_alunos(res: Response) -> list:
    alunos = await Aluno_CRUD.getAllAlunos() 
    
    if alunos is None or alunos is []:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return alunos

@router_usuario.post('/createAluno')
async def create_aluno(new_aluno: list[Aluno], res: Response) -> dict:
    if not new_aluno or new_aluno is []:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Aluno_CRUD.createAluno(new_aluno)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]


@router_usuario.put('/updateAluno/{id}') 
async def update_aluno(id: int, new_values: Aluno, res: Response) -> dict:
    if not new_values:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Aluno_CRUD.updateAluno(id, new_values)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code  = status.HTTP_200_OK
    return messages["sucess"]

@router_usuario.delete('/deleteAluno/{id}')
async def delete(id: int, res: Response) -> dict:
    if id <= 0 or id is None:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Aluno_CRUD.deleteAluno(id)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]