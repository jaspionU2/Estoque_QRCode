from fastapi import APIRouter, Response, status, Depends
from model.Model_serie import Serie
from services.Serie_service import Serie_CRUD  

from configs import statusMessage
from configs.security import get_current_user

router_serie = APIRouter()  

@router_serie.get("/getAllSeries")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    series = await Serie_CRUD.getAllSeries()
    
    if series is None or series is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return series

@router_serie.post("/addNewSerie")
async def create(
    new_serie: list[Serie],
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if new_serie is None or new_serie is []:
        raise statusMessage.NOT_DATA
    
    result = await Serie_CRUD.createMateria(new_serie)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_201_CREATED

@router_serie.delete("/deleteOneSerie")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if id is None or id <= 0:
        raise statusMessage.NOT_DATA
    
    result = await Serie_CRUD.deleteMateria(id)
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED