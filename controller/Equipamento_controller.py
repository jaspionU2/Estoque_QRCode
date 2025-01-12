from fastapi import APIRouter, Response, status, Depends
from services.Equipamento_service import Equipmanento_CRUD
from model.Model_Equipamento import Equipamento

from configs.security import get_current_user

from configs.statusMessage import messages

router_equipamentos = APIRouter()  

@router_equipamentos.get('/getAllEquipamentos')
async def get(
    res: Response,
    current_user = Depends(get_current_user)
):
    equipamentos = await Equipmanento_CRUD.getAllEquipamentos()
    
    if not equipamentos:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
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
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]

    sucess = await Equipmanento_CRUD.createEquipamento(new_equipmanento)
    
    if not sucess:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
        
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]
    
@router_equipamentos.put("/updateEquipamento/{id}")
async def update(
    id: int,
    new_values: Equipamento,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if not new_values:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Equipmanento_CRUD.updateEquipamento(id, new_values)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code  = status.HTTP_200_OK
    return messages["sucess"]
    
@router_equipamentos.delete("/deleteEquipamento/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Equipmanento_CRUD.deleteEquipamento(id) 
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]
