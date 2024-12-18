from fastapi import APIRouter, Response, status  
from services.Usuarios_service import Aluno_CRUD, Professor_CRUD
from model.Model_Aluno import Aluno
from model.Model_Professor import Professor


router_usuario = APIRouter()  

@router_usuario.get('/getAllProfessores')
async def get_Professores(res: Response) -> list[Professor]:
    professores = await Professor_CRUD.getAllProfessores()

    if professores == None:
        res.status_code = status.HTTP_404_NOT_FOUND
        return None
    
    res.status_code = status.HTTP_200_OK
    return professores

@router_usuario.post('/createProfessor')
async def create_professor(new_professor: dict, res: Response) -> dict:
    if not new_professor or new_professor is {}: 
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "status": res.status_code,
            "message": "Ausencia de dados",
            "created": False
        }
        
    success = await Professor_CRUD.createProfessor(new_professor)
    
    if not success:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": res.status_code,
            "message": "Erro no processamento",
            "created": False
        }
        
    res.status_code = status.HTTP_201_CREATED
    return {
        "status": res.status_code,
        "created": True
    }

@router_usuario.put('/updateProfessor/{id}') 
async def update_Professor(id: int, new_values: dict, res: Response) -> dict:
    if not new_values:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "status": res.status_code,
            "message": "Ausencia de dados",
            "updated": False
        }
    
    result = await Professor_CRUD.updateProfessor(id, new_values)
    if not result:
        res.status_code = status.HTTP_409_CONFLICT
        return {
            "status": res.status_code,
            "message": "Erro ao atualizar os dados solicitados",
            "updated": False
        }
        
    res.status_code = status.HTTP_200_OK
    return {}

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
async def create_aluno(new_aluno: list[Aluno], res: Response) -> dict:
    if not new_aluno or new_aluno is {}:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "status": res.status_code,
            "message": "Ausencia de dados",
            "created": False
        }
    
    success = await Aluno_CRUD.createAluno(new_aluno)
    
    if not success:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": res.status_code,
            "message": "Erro no processamento",
            "created": False
        }
        
    res.status_code = status.HTTP_201_CREATED
    return {
        "status": res.status_code,
        "created": True
    }


@router_usuario.put('/updateAluno/{id}') 
async def update_aluno(id: int, new_values: Aluno, res: Response) -> dict:
    if not new_values:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "status": res.status_code,
            "message": "Ausencia de dados",
            "updated": False
        }
    
    result = await Aluno_CRUD.updateAluno(id, new_values)
    
    if not result:
        res.status_code = status.HTTP_409_CONFLICT
        return {
            "status": res.status_code,
            "message": "Erro ao atualizar os dados solicitados",
            "updated": False
        }
        
    res.status_code = status.HTTP_200_OK
    return {
        "status": res.status_code,
        "updated": True
    }

@router_usuario.delete('/deleteAluno/{id}')
async def delete(id: int, res: Response) -> dict:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {
            "status": res.status_code,
            "message": "Ausencia de dados",
            "deleted": False
        }
    
    deleted = await Aluno_CRUD.deleteAluno(id)
    
    if not deleted:
        res.status_code = status.HTTP_409_CONFLICT
        return {
            "status": res.status_code,
            "message": "Erro ao deletar a entidade",
            "deleted": False
        }
        
    res.status_code = status.HTTP_200_OK
    return {
        "status": res.status_code,
        "deleted": True
    }