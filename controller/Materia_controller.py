from fastapi import APIRouter, Response, status  

router_materia = APIRouter()  

@router_materia.get("/getAllMaterias")
async def get(res: Response) -> list:
    materias = [""] # service.getAllMaterias()
    return materias

@router_materia.post("/addNewMateria")
async def create(new_materia: dict, res: Response) -> None:
    if new_materia == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.createNewMateria(new_materia.value)

@router_materia.delete("/deleteOneMateria")
async def delete(materia: dict, res: Response) -> None:
    if materia == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.deleteMateria(materia.value)