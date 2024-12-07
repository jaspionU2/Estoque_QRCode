from fastapi import APIRouter, Response, status  

router_status_dispositivo = APIRouter()  

@router_status_dispositivo.get("/getAllStatus")
async def get(res: Response) -> list:
    status_dispositivo = [""] # service.getAllStatus_dispositivo()
    return status_dispositivo

@router_status_dispositivo.post("/addNewStatus_dispositivo")
async def create(new_status_dispositivo: dict, res: Response) -> None:
    if new_status_dispositivo == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.createNewStatus_dispositivo(new_status_dispositivo.value)

@router_status_dispositivo.delete("/deleteOneStatus_dispositivo")
async def delete(status_dispositivo: dict, res: Response) -> None:
    if status_dispositivo == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.deleteStatus_dispositivo(status_dispositivo.value)