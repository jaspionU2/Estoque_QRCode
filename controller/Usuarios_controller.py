from fastapi import APIRouter, Response, status  
from services.Usuarios_service import Aluno_CRUD, Professor_CRUD
from model.Model_Aluno import Aluno
from model.Model_Professor import Professor


router_usuario = APIRouter()  

@router_usuario.get('/getAllProfessores')
async def get_Professores(res: Response) -> list:
    professores = await Professor_CRUD.getAllProfessores()
    res.status_code = status.HTTP_200_OK
    return professores

@router_usuario.post('/createProfessor')
async def create_professor(new_professores: list[dict], res: Response):
    if not new_professores: 
        res.status_code = status.HTTP_400_BAD_REQUEST
        return
        
    success = await Professor_CRUD.createProfessor(new_professores)
    
    if success:
        res.status_code = status.HTTP_201_CREATED
        return
    else:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return

@router_usuario.put('/updateProfessor/{id}') 
async def update_Professor(id: int, new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Professor_CRUD.updateProfessor(id, new_values)
    res.status_code = status.HTTP_200_OK

@router_usuario.delete('/deleteProfessor/{id}')
async def delete(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    await Professor_CRUD.deleteProfessor(id)
    res.status_code = status.HTTP_200_OK

@router_usuario.get('/getAllAlunos')
async def get_alunos(res: Response) -> list:
    Alunos = await Aluno_CRUD.getAllAlunos() 
    res.status_code = status.HTTP_200_OK
    return Alunos

@router_usuario.post('/createAluno')
async def create_aluno(new_aluno: list[Aluno], res: Response) -> None:
    if not new_aluno :
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    sucess = await Aluno_CRUD.createAluno(new_aluno)
    
    if sucess:
        res.status_code = status.HTTP_201_CREATED
        return
    else:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return

@router_usuario.put('/updateAluno/{id}') 
async def update_aluno(id: int, new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Aluno_CRUD.updateAluno(id, new_values)
    res.status_code = status.HTTP_200_OK

@router_usuario.delete('/deleteAluno/{id}')
async def delete(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    await Aluno_CRUD.deleteAluno(id)
    res.status_code = status.HTTP_200_OK