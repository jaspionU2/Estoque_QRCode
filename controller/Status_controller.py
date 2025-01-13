from fastapi import APIRouter, Response, status, Depends  
from services.Status_service import Status_CRUD

from configs import statusMessage
from configs.security import get_current_user

router_status_dispositivo = APIRouter()  

@router_status_dispositivo.get("/getAllStatus")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    status_dispositivo = await Status_CRUD.getAllStatus()
    
    if status_dispositivo is None or status_dispositivo is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return status_dispositivo

@router_status_dispositivo.post("/addNewStatus_dispositivo")
async def create(
    new_status_dispositivo: list[dict],
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if new_status_dispositivo is None or new_status_dispositivo is []:
        raise statusMessage.NOT_DATA
    
    result = await Status_CRUD.createStatus(new_status_dispositivo)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_201_CREATED

@router_status_dispositivo.delete("/deleteOneStatus_dispositivo/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if id is None or id < 1:
        raise statusMessage.NOT_DATA
    
    result = await Status_CRUD.deleteStatus(id)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED