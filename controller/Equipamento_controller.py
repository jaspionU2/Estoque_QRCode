from fastapi import APIRouter, Response, status
from services.Equipamento_service import Equipmanento_CRUD
from model.Model_Equipamento import Equipamento

router_equipamentos = APIRouter()  

@router_equipamentos.get('/getAllEquipamentos')
async def get(res: Response) -> list:
    equipamentos = await Equipmanento_CRUD.getAllEquipamentos()
    
    if equipamentos is None:
        res.status_code = status.HTTP_404_NOT_FOUND
        return None
    
    res.status_code = status.HTTP_200_OK
    return equipamentos

@router_equipamentos.post('/createEquipmanento')
async def create(tipo_equipamento: int, new_equipmanento: list[Equipamento], res: Response):
    if new_equipmanento == None:
        res.status_code = status.HTTP_400_BAD_REQUEST

    await Equipmanento_CRUD.createEquipamento(new_equipmanento)
    
@router_equipamentos.put("/updateEquipamento/{id}")
async def update(id: int, new_values: Equipamento, res: Response):
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Equipmanento_CRUD.updateEquipamento(id, new_values)
    
@router_equipamentos.delete("/deleteEquipamento/{id}")
async def delete(id: int, res: Response):
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    await Equipmanento_CRUD.deleteEquipamento(id) 
    res.status_code = status.HTTP_200_OK
