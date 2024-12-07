from fastapi import APIRouter, Response, status  

router_serie = APIRouter()  

@router_serie.get("/getAllSeries")
async def get(res: Response) -> list:
    series = [""] # service.getAllSeries()
    return series

@router_serie.post("/addNewSerie")
async def create(new_serie: dict, res: Response) -> None:
    if new_serie == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.createNewSerie(new_serie.value)

@router_serie.delete("/deleteOneSerie")
async def delete(serie: dict, res: Response) -> None:
    if serie == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.deleteSerie(serie.value)