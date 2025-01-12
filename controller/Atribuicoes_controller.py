from fastapi import APIRouter, Response, status, Depends

from services.Atribuicoes_service import Atribuicao_CRUD

from model.Model_Atribuicao_permanente import Atribuicao_permanente as Atribuicao

from configs.security import get_current_user

from configs.statusMessage import messages

router_atribuicao = APIRouter()  

@router_atribuicao.get('/getAllAtribuicoesFromAlunos')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    atribuicoes = await Atribuicao_CRUD.getAllAtrubuicoesFromAlunos()
    
    if not atribuicoes:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
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
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return atribuicoes

@router_atribuicao.post('/createNewAtribuicao')
async def create(
    new_atribuicao: dict,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if not new_atribuicao or new_atribuicao is {}: 
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    sucess = Atribuicao_CRUD.createAtricuicao(new_atribuicao)
    
    if not sucess:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
        
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]

@router_atribuicao.put('/updateAtribuicao')
async def update(
    new_values: dict,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if not new_values:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = Atribuicao_CRUD.updateAtribuicao(new_values["id"], new_values)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
        
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]
    
@router_atribuicao.delete('/deleteAtribuicao/{id}')
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    
    deleted = Atribuicao_CRUD.deleteAtribuicao(id)
    if not deleted:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
        
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]
    
    
