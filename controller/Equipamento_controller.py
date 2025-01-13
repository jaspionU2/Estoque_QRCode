from fastapi import APIRouter, Response, status, Depends
from services.Equipamento_service import Equipmanento_CRUD
from model.Model_Equipamento import Equipamento

from configs.security import get_current_user

from configs import statusMessage

router_equipamentos = APIRouter()  

@router_equipamentos.get('/getAllEquipamentos')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
):
    equipamentos = await Equipmanento_CRUD.getAllEquipamentos()
    
    if not equipamentos:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return equipamentos

@router_equipamentos.post('/createEquipmanento')
async def create(
    tipo_equipamento: int,
    new_equipmanento: list[Equipamento],
    res: Response,
    current_user = Depends(get_current_user)
):
    if new_equipmanento is None or new_equipmanento is []:
        raise statusMessage.NOT_DATA

    sucess = await Equipmanento_CRUD.createEquipamento(new_equipmanento)
    
    if not sucess:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_201_CREATED
    
@router_equipamentos.put("/updateEquipamento/{id}")
async def update(
    id: int,
    new_values: Equipamento,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if not new_values:
        raise statusMessage.NOT_DATA
    
    result = await Equipmanento_CRUD.updateEquipamento(id, new_values)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code  = status.HTTP_202_ACCEPTED
    
@router_equipamentos.delete("/deleteEquipamento/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if id <= 0 or id == None:
        raise statusMessage.NOT_DATA
    
    result = await Equipmanento_CRUD.deleteEquipamento(id) 
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED
