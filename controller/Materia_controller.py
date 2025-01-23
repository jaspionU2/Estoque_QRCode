from fastapi import APIRouter, Response, status, Depends
from service.Materia_service import Materia_CRUD
from model.Model_Materia import Materia  

from configs import statusMessage
from configs.security import get_current_user

router_materia = APIRouter()  

@router_materia.get("/getAllMaterias")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    
    materias = Materia_CRUD.getAllMaterias()
    
    if materias is None or materias is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return materias

@router_materia.post("/addNewMateria")
async def create(
    new_materia: list[Materia],
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if new_materia is None or new_materia is []:
        raise statusMessage.NOT_DATA
    
    result = await Materia_CRUD.createMateria(new_materia)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_201_CREATED

@router_materia.delete("/deleteOneMateria/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if id == None and id <= 0:
        raise statusMessage.NOT_DATA
    
    result = await Materia_CRUD.deleteMateria(id)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED