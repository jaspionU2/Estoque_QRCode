from fastapi import APIRouter, Response, status, Depends

from service.Atribuicoes_service import Atribuicao_CRUD

from model.Model_Atribuicao_permanente import Atribuicao_permanente as Atribuicao

from configs.security import get_current_user

from configs import statusMessage

router_atribuicao = APIRouter()  

@router_atribuicao.get('/getAllAtribuicoesFromAlunos')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    atribuicoes = await Atribuicao_CRUD.getAllAtrubuicoesFromAlunos()
    
    if not atribuicoes:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return atribuicoes

@router_atribuicao.get('/getAllAtribuicoesFromProfessores')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    atribuicoes = await Atribuicao_CRUD.getAllAtrubuicoesFromProfessores()
    print(atribuicoes)
    
    if not atribuicoes:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return atribuicoes

@router_atribuicao.post('/createNewAtribuicao')
async def create(
    new_atribuicao: dict,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if not new_atribuicao or new_atribuicao is {}: 
        raise statusMessage.NOT_DATA
    
    sucess = Atribuicao_CRUD.createAtricuicao(new_atribuicao)
    
    if not sucess:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_201_CREATED

@router_atribuicao.put('/updateAtribuicao')
async def update(
    new_values: dict,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if not new_values:
        raise statusMessage.NOT_DATA
    
    result = Atribuicao_CRUD.updateAtribuicao(new_values["id"], new_values)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_202_ACCEPTED
    
@router_atribuicao.delete('/deleteAtribuicao/{id}')
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    
    if id <= 0 or id == None:
        raise statusMessage.NOT_DATA
    
    
    deleted = Atribuicao_CRUD.deleteAtribuicao(id)
    
    if not deleted:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_202_ACCEPTED