from fastapi import APIRouter, Response, status, Depends, HTTPException

from service.Atribuicoes_service import Atribuicao_CRUD

from configs.security import get_current_user
from configs.customExceptions import CustomSQLException
from configs import statusMessage

from sqlalchemy.exc import SQLAlchemyError

from schema.Schema_Emprestimo_Atribuicao import SchemaAtribuicao, SchemaAtribuicaoPublico

router_atribuicao = APIRouter()  

@router_atribuicao.get('/getAllAtribuicoesFromAlunos')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    
    result_atribuicao = await Atribuicao_CRUD.getAllAtrubuicoesFromAlunos()
    
    if not result_atribuicao:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return result_atribuicao

@router_atribuicao.get('/getAllAtribuicoesFromProfessores')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    
    result_atribuicao = await Atribuicao_CRUD.getAllAtrubuicoesFromProfessores()
 
    if not result_atribuicao:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    
    return result_atribuicao


@router_atribuicao.post('/createNewAtribuicao', response_model=SchemaAtribuicaoPublico)
async def create(
    new_atribuicao: SchemaAtribuicao,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaAtribuicaoPublico:
    
    if not new_atribuicao or new_atribuicao is {}: 
        raise statusMessage.NOT_DATA
    
    result_atribuicao = await Atribuicao_CRUD.createAtribuicao(new_atribuicao.model_dump())
    
    if isinstance(result_atribuicao, CustomSQLException):
        
        raise HTTPException(
            status_code=statusMessage.INTERNAL_SERVER_ERROR.status_code,
            detail=result_atribuicao.get_argument()
        )
    
    # if isinstance(result_atribuicao, dict) and result_atribuicao.get('type_exception') is 'SQLAlchemyError':
        
    #     raise HTTPException(
    #         status_code=statusMessage.INTERNAL_SERVER_ERROR.status_code,
    #         detail=result_atribuicao.get('details')
    #     )
    
    if not result_atribuicao:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_201_CREATED
    
    return result_atribuicao
    
@router_atribuicao.put('/updateAtribuicao/{id}', response_model=SchemaAtribuicaoPublico)
async def update(
    id: int,
    new_values: SchemaAtribuicao,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaAtribuicaoPublico:
    
    if not new_values:
        raise statusMessage.NOT_DATA
    
    result_atribuicao = Atribuicao_CRUD.updateAtribuicao(id, new_values.model_dump())
    
    if not result_atribuicao:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_202_ACCEPTED
    
    return result_atribuicao
    
@router_atribuicao.delete('/deleteAtribuicao/{id}')
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    
    if id <= 0 or id == None:
        raise statusMessage.NOT_DATA
    
    
    result_deleted = Atribuicao_CRUD.deleteAtribuicao(id)
    
    if not result_deleted:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_202_ACCEPTED