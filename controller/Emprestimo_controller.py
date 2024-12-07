from fastapi import APIRouter, Response, status  

router_emprestimo = APIRouter()  

@router_emprestimo.get('/getAllEmprestimos')
async def get(res: Response) -> list:
    emprestimos = [{}] #service.getAllEmprestimosFromAluno
    emprestimos.append([{}]) #service.getAllEmprestimosFromProfessor
    res.status_code = status.HTTP_200_OK
    return emprestimos

@router_emprestimo.get('/getAllEmprestimosFromAlunos')
async def get(res: Response) -> list:
    emprestimos = [{}] #service.getAllEmprestimosFromAluno
    res.status_code = status.HTTP_200_OK
    return emprestimos

@router_emprestimo.get('/getAllEmprestimosFromProfessores')
async def get(res: Response) -> list:
    emprestimos = [{}] #service.getAllEmprestimosFromProfessor
    res.status_code = status.HTTP_200_OK
    return emprestimos

@router_emprestimo.post('/createNewEmprestimo')
async def create(new_emprestimo: dict, res: Response) -> None:
    if new_emprestimo == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.createEmprestimo(new_emprestimo)
    res.status_code = status.HTTP_201_CREATED

@router_emprestimo.put('/updateEmprestimo')
async def update(new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.updateEmprestimo(new_values)
    res.status_code = status.HTTP_200_OK
    
@router_emprestimo.delete('/deleteEmprestimo/{id}')
async def delete(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    # sevice.deleteEmprestimo(id)
    res.status_code = status.HTTP_200_OK