from fastapi import APIRouter, Response, status
from model.Model_serie import Serie
from services.Serie_service import Serie_CRUD  

router_serie = APIRouter()  

@router_serie.get("/getAllSeries")
async def get(res: Response) -> list:
    series = await Serie_CRUD.getAllSeries()
    return series

@router_serie.post("/addNewSerie")
async def create(new_serie: list[Serie], res: Response) -> None:
    if new_serie == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Serie_CRUD.createMateria(new_serie)

@router_serie.delete("/deleteOneSerie")
async def delete(id: int, res: Response) -> None:
    
    if id == None and id < 1:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Serie_CRUD.deleteMateria(id)