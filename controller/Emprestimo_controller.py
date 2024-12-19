from fastapi import APIRouter, Response, status  
from services.Emprestimo_service import Emprestimo_CRUD
from model.Model_Emprestimo import Emprestimo

from configs.statusMessage import messages

router_emprestimo = APIRouter()  

@router_emprestimo.get('/getAllEmprestimosFromAlunos')
async def get(res: Response) -> list[dict]:
    emprestimos = await Emprestimo_CRUD.getAllEmprestimosFromAlunos()
    
    if emprestimos is None or emprestimos is []:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return emprestimos

@router_emprestimo.get('/getAllEmprestimosFromProfessores')
async def get(res: Response) -> list[dict]:
    emprestimos = await Emprestimo_CRUD.getAllEmprestimosFromProfessores()
    
    if emprestimos is None or emprestimos is []:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return emprestimos

@router_emprestimo.post('/createNewEmprestimo')
async def create(new_emprestimo: list[Emprestimo], res: Response) -> dict:
    if not new_emprestimo or new_emprestimo is {}: 
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
        
    success = await Emprestimo_CRUD.createEmprestimo(new_emprestimo)
    
    if not success:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
        
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]

@router_emprestimo.put('/updateEmprestimo')
async def update(id: int, new_values: dict, res: Response) -> dict:
    if not new_values:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Emprestimo_CRUD.updateEmprestimo(id, new_values)
    
    if not result:
        res.status_code = status.HTTP_409_CONFLICT
        return messages["not_sucess"]
        
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]
    
@router_emprestimo.delete('/deleteEmprestimo/{id}')
async def delete(id: int, res: Response) -> dict:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return messages["not_data"]
    
    deleted = await Emprestimo_CRUD.deleteEmprestimo(id)
    
    if not deleted:
        res.status_code = status.HTTP_409_CONFLICT
        return messages["not_sucess"]
        
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]