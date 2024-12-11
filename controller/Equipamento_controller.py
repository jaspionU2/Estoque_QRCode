from fastapi import APIRouter, Response, status
from services.Equipamento_service import Equipmanento_CRUD
from model.Model_Equipamento import Equipamento

router_equipamentos = APIRouter()  

@router_equipamentos.get('/getAllEquipamentos')
async def get(res: Response) -> list:
    equipamentos = await Equipmanento_CRUD.getAllEquipamentos()
    res.status_code = status.HTTP_200_OK
    return equipamentos

@router_equipamentos.post('/createEquipmanento')
async def create_chrome(new_equipmanento: list[Equipamento], res: Response) -> None:
    if new_equipmanento == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None

    await Equipmanento_CRUD.createEquipamento(new_equipmanento)
    
@router_equipamentos.put("/updateEquipamento/{id}")
async def update_chrome(id: int, new_values: Equipamento, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Equipmanento_CRUD.updateEquipamento(id, new_values)
    
@router_equipamentos.delete("/deleteEquipamento/{id}")
async def delete_chrome(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    await Equipmanento_CRUD.deleteEquipamento(id) 
    res.status_code = status.HTTP_200_OK
