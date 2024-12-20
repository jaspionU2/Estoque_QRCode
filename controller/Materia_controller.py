from fastapi import APIRouter, Response, status
from services.Materia_service import Materia_CRUD
from model.Model_Materia import Materia  

from configs.statusMessage import messages

router_materia = APIRouter()  

@router_materia.get("/getAllMaterias")
async def get(res: Response) -> list:
    materias = await Materia_CRUD.getAllMaterias()
    
    if materias is None or materias is []:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return materias

@router_materia.post("/addNewMateria")
async def create(new_materia: list[Materia], res: Response) -> dict:
    if new_materia is None or new_materia is []:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Materia_CRUD.createMateria(new_materia)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]

@router_materia.delete("/deleteOneMateria/{id}")
async def delete(id: int, res: Response) -> dict:
    if id == None and id <= 0:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Materia_CRUD.deleteMateria(id)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]