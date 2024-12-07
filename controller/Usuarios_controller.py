from fastapi import APIRouter, Response, status  

router_usuario = APIRouter()  

@router_usuario.get('/getAllProfessores')
async def get_Professores(res: Response) -> list:
    professores = [{}] #service.getAllProfessores()
    res.status_code = status.HTTP_200_OK
    return professores

@router_usuario.post('/createProfessor')
async def create_Professor(new_professor: dict, res: Response) -> None:
    if new_professor == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.createProfessor(new_professor)
    res.status_code = status.HTTP_201_CREATED

@router_usuario.put('/updateProfessor') 
async def update_Professor(new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.updateProfessor(new_values)
    res.status_code = status.HTTP_200_OK

@router_usuario.delete('/deleteProfessor/{id}')
async def delete(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    # sevice.deleteProfessor(id)
    res.status_code = status.HTTP_200_OK

@router_usuario.get('/getAllAlunos')
async def get_alunos(res: Response) -> list:
    Alunos = [{}] #service.getAllAlunos()
    res.status_code = status.HTTP_200_OK
    return Alunos

@router_usuario.post('/createAluno')
async def create_aluno(new_aluno: dict, res: Response) -> None:
    if new_aluno == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.createAluno(new_aluno)
    res.status_code = status.HTTP_201_CREATED

@router_usuario.put('/updateAluno') 
async def update_aluno(new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.updateAluno(new_values)
    res.status_code = status.HTTP_200_OK

@router_usuario.delete('/deleteAluno/{id}')
async def delete(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    # sevice.deleteAluno(id)
    res.status_code = status.HTTP_200_OK