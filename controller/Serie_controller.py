from fastapi import APIRouter, Response, status, Depends
from model.Model_serie import Serie
from services.Serie_service import Serie_CRUD  

from configs.statusMessage import messages
from configs.security import get_current_user

router_serie = APIRouter()  

@router_serie.get("/getAllSeries")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    series = await Serie_CRUD.getAllSeries()
    
    if series is None or series is []:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return series

@router_serie.post("/addNewSerie")
async def create(
    new_serie: list[Serie],
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if new_serie is None or new_serie is []:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Serie_CRUD.createMateria(new_serie)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]

@router_serie.delete("/deleteOneSerie")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if id is None or id <= 0:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Serie_CRUD.deleteMateria(id)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]