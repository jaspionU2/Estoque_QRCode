from fastapi import APIRouter, Response, status, Depends  
from services.Status_service import Status_CRUD

from configs.statusMessage import messages
from configs.security import get_current_user

router_status_dispositivo = APIRouter()  

@router_status_dispositivo.get("/getAllStatus")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    status_dispositivo = await Status_CRUD.getAllStatus()
    
    if status_dispositivo is None or status_dispositivo is []:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return status_dispositivo

@router_status_dispositivo.post("/addNewStatus_dispositivo")
async def create(
    new_status_dispositivo: list[dict],
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if new_status_dispositivo is None or new_status_dispositivo is []:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Status_CRUD.createStatus(new_status_dispositivo)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]

@router_status_dispositivo.delete("/deleteOneStatus_dispositivo/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if id is None or id < 1:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Status_CRUD.deleteStatus(id)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]