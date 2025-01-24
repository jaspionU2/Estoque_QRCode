from fastapi import APIRouter, Response, status, Depends
from model.Model_serie import Serie
from service.Serie_service import Serie_CRUD  

from configs import statusMessage
from configs.security import get_current_user

from schema.Schema_Status_Categoria_Serie_Materia import SchemaSerie, SchemaSeriePublico

router_serie = APIRouter()  

@router_serie.get("/getAllSeries")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    
    result_serie = await Serie_CRUD.getAllSeries()
    
    if result_serie is None or result_serie is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return result_serie

@router_serie.post("/addNewSerie", response_model=SchemaSeriePublico)
async def create(
    new_serie: SchemaSerie,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaSeriePublico:
    
    if new_serie is None or new_serie is []:
        raise statusMessage.NOT_DATA
    
    result_serie = await Serie_CRUD.createSerie(new_serie.model_dump())
    
    if not result_serie:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_201_CREATED

@router_serie.delete("/deleteOneSerie")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if id is None or id <= 0:
        raise statusMessage.NOT_DATA
    
    result_serie = await Serie_CRUD.deleteSerie(id)
    
    if not result_serie:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED