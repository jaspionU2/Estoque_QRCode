from fastapi import APIRouter, Response, status
from services.Materia_service import Materia_CRUD
from model.Model_Materia import Materia  

router_materia = APIRouter()  

@router_materia.get("/getAllMaterias")
async def get(res: Response) -> list:
    materias = await Materia_CRUD.getAllMaterias()
    return materias

@router_materia.post("/addNewMateria")
async def create(new_materia: list[Materia], res: Response) -> None:
    if new_materia == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Materia_CRUD.createMateria(new_materia)

@router_materia.delete("/deleteOneMateria/{id}")
async def delete(id: int, res: Response) -> None:
    if id == None and id < 0:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Materia_CRUD.deleteMateria(id)