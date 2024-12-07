from fastapi import APIRouter, Response, status  

router_atribuicao = APIRouter()  

@router_atribuicao.get('/getAllAtribuicoes')
async def get(res: Response) -> list:
    atribuicoes = [{}] #service.getAllAtribuicoesFromAluno
    atribuicoes.append([{}]) #service.getAllAtribuicoesFromProfessor
    res.status_code = status.HTTP_200_OK
    return atribuicoes

@router_atribuicao.get('/getAllAtribuicoesFromAlunos')
async def get(res: Response) -> list:
    atribuicoes = [{}] #service.getAllAtribuicoesFromAluno
    res.status_code = status.HTTP_200_OK
    return atribuicoes

@router_atribuicao.get('/getAllAtribuicoesFromProfessores')
async def get(res: Response) -> list:
    atribuicoes = [{}] #service.getAllAtribuicoesFromProfessor
    res.status_code = status.HTTP_200_OK
    return atribuicoes

@router_atribuicao.post('/createNewAtribuicao')
async def create(new_atribuicao: dict, res: Response) -> None:
    if new_atribuicao == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.createAtribuicao(new_atribuicao)
    res.status_code = status.HTTP_201_CREATED

@router_atribuicao.put('/updateAtribuicao')
async def update(new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.updateAtribuicao(new_values)
    res.status_code = status.HTTP_200_OK
    
@router_atribuicao.delete('/deleteAtribuicao/{id}')
async def delete(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    # sevice.deleteAtribuicao(id)
    res.status_code = status.HTTP_200_OK
    
    
