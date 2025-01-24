from fastapi import APIRouter, Response, status, Depends  
from service.Status_service import Status_CRUD

from configs import statusMessage
from configs.security import get_current_user

from schema.Schema_Status_Categoria_Serie_Materia import SchemaStatus, SchemaStatusPublico

router_status_dispositivo = APIRouter()  

@router_status_dispositivo.get("/getAllStatus")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    
    result_status = await Status_CRUD.getAllStatus()
    
    if result_status is None or result_status is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return result_status

@router_status_dispositivo.post("/addNewStatus_dispositivo", response_model=SchemaStatusPublico)
async def create(
    new_status_dispositivo: SchemaStatus,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaStatusPublico:
    
    if new_status_dispositivo is None or new_status_dispositivo is []:
        raise statusMessage.NOT_DATA
    
    result_status = await Status_CRUD.createStatus(new_status_dispositivo.model_dump())
    
    if not result_status:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_201_CREATED
    return result_status

@router_status_dispositivo.delete("/deleteOneStatus_dispositivo/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    
    if id is None or id < 1:
        raise statusMessage.NOT_DATA
    
    result_status = await Status_CRUD.deleteStatus(id)
    
    if not result_status:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED