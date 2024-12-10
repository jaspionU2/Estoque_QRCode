from fastapi import APIRouter, Response, status  
from services.Status_service import Status_CRUD

router_status_dispositivo = APIRouter()  

@router_status_dispositivo.get("/getAllStatus")
async def get(res: Response) -> list:
    status_dispositivo = await Status_CRUD.getAllStatus()
    return status_dispositivo

@router_status_dispositivo.post("/addNewStatus_dispositivo")
async def create(new_status_dispositivo: list[dict], res: Response) -> None:
    if new_status_dispositivo == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Status_CRUD.createStatus(new_status_dispositivo)

@router_status_dispositivo.delete("/deleteOneStatus_dispositivo{id}")
async def delete(id: int, res: Response) -> None:
    if id == None and id < 1:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Status_CRUD.deleteStatus(id)