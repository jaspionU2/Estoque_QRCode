from fastapi import APIRouter, Response, status, Depends 
from service.Emprestimo_service import Emprestimo_CRUD

from configs import statusMessage
from configs.security import get_current_user

from schema.Schema_Emprestimo_Atribuicao import SchemaEmprestimo, SchemaEmprestimoPublico

router_emprestimo = APIRouter()  

@router_emprestimo.get('/getAllEmprestimosFromAlunos')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    result_emprestimo = await Emprestimo_CRUD.getAllEmprestimosFromAlunos()
    
    if result_emprestimo is None or result_emprestimo is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return result_emprestimo

@router_emprestimo.get('/getAllEmprestimosFromProfessores')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    
    result_emprestimo = await Emprestimo_CRUD.getAllEmprestimosFromProfessores()
    
    if result_emprestimo is None or result_emprestimo is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return result_emprestimo

@router_emprestimo.post('/createNewEmprestimo', response_model=SchemaEmprestimoPublico)
async def create(
    new_emprestimo: SchemaEmprestimo,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaEmprestimoPublico:
    
    if not new_emprestimo or new_emprestimo is {}: 
        raise statusMessage.NOT_DATA
        
    result_emprestimo = await Emprestimo_CRUD.createEmprestimo(new_emprestimo.model_dump())
    
    if not result_emprestimo:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_201_CREATED
    
    return result_emprestimo

@router_emprestimo.put('/updateEmprestimo')
async def update(
    id: int,
    new_values: dict,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if not new_values:
        raise statusMessage.NOT_DATA
    
    result_emprestimo = await Emprestimo_CRUD.updateEmprestimo(id, new_values)
    
    if not result_emprestimo:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_202_ACCEPTED
    
    return result_emprestimo
    
@router_emprestimo.delete('/deleteEmprestimo/{id}')
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if id <= 0 or id == None:
        raise statusMessage.NOT_DATA
    
    result_delete = await Emprestimo_CRUD.deleteEmprestimo(id)
    
    if not result_delete:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_202_ACCEPTED