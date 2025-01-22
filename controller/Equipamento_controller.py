from fastapi import APIRouter, Response, status, Depends

from service.Equipamento_service import Equipamento_CRUD

from configs.security import get_current_user

from configs import statusMessage

from schema.Schema_Equipamento import SchemaEquipamento, SchemaEquipamentoPublico

router_equipamentos = APIRouter()  

@router_equipamentos.get('/getAllEquipamentos')
async def get_all_equipamentos(
    res: Response,
    current_user=Depends(get_current_user)
) -> list:
    
    result = Equipamento_CRUD.getAllEquipamentos()
    
    if result == []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return result

@router_equipamentos.post('/createEquipmanento', response_model=SchemaEquipamentoPublico)
async def create(
    new_equipmanento: SchemaEquipamento,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaEquipamentoPublico:
    
    if new_equipmanento is None or new_equipmanento is []:
        raise statusMessage.NOT_DATA

    result =  Equipamento_CRUD.createEquipamento(new_equipmanento.model_dump())
    
    if not result:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_201_CREATED
    
    return result
    
@router_equipamentos.put("/updateEquipamento/{id}", response_model=SchemaEquipamentoPublico)
async def update(
    id: int,
    new_values: SchemaEquipamento,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaEquipamentoPublico:
    
    if not new_values:
        raise statusMessage.NOT_DATA
    
    result =  Equipamento_CRUD.updateEquipamento(id, new_values.model_dump())
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code  = status.HTTP_202_ACCEPTED
    
    return result
    
@router_equipamentos.delete("/deleteEquipamento/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if id <= 0 or id == None:
        raise statusMessage.NOT_DATA
    
    result =  Equipamento_CRUD.deleteEquipamento(id) 
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED
