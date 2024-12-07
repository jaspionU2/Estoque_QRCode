from fastapi import APIRouter, Response, status  

router_equipamentos = APIRouter()  

@router_equipamentos.get('/getAllEquipamentos')
async def get(res: Response) -> list:
    equipamentos = [{}] #service.getAllEquipametos
    res.status_code = status.HTTP_200_OK
    return equipamentos

@router_equipamentos.post('/createChromebook')
async def create_chrome(new_chrome: dict, res: Response) -> None:
    if new_chrome == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None

    # service.createNewChrome(new_chrome)

@router_equipamentos.post('/createIpad')
async def create_ipad(new_ipad: dict, res: Response) -> None:
    if new_ipad == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None

    # service.createNewIpad(new_ipad)

@router_equipamentos.post('/createCarregador')
async def create_ipad(new_carregador: dict, res: Response) -> None:
    if new_carregador == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None

    # service.createNewCarregador(new_carregador)
    
@router_equipamentos.put("/updateChromeBook")
async def update_chrome(new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    #service.updateChrome(new_values)

@router_equipamentos.put("/updateIpad")
async def update_ipad(new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    #service.updateIpad(new_values)

@router_equipamentos.put("/updateCarregador")
async def update_caregador(new_values: dict, res: Response) -> None:
    if new_values == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    #service.updateCarregador(new_values)
    
@router_equipamentos.delete("/deleteChomebook/{id}")
async def delete_chrome(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    # sevice.deleteChromeBook(id)
    res.status_code = status.HTTP_200_OK
    
@router_equipamentos.delete("/deleteIpad/{id}")
async def delete_ipad(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    # sevice.deleteIpad(id)
    res.status_code = status.HTTP_200_OK

@router_equipamentos.delete("/deleteCarregador/{id}")
async def delete_carregador(id: int, res: Response) -> None:
    if id <= 0 or id == None:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return None
    
    # sevice.deleteCarregador(id)
    res.status_code = status.HTTP_200_OK  