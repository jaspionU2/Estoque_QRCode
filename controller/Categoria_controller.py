from fastapi import APIRouter, Response, status, Depends 
from services.Categorias_service import Categoria_CRUD

from configs import statusMessage
from configs.security import get_current_user

from model.Model_Categoria import Categoria

router_categoria = APIRouter()  

@router_categoria.get("/getAllCategorias")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list[dict]:
    categorias = await Categoria_CRUD.getAllCategorias()
    if categorias is None or categorias is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return categorias

@router_categoria.post("/addNewCategoria")
async def create(
    new_categoria: list[Categoria],
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if new_categoria is None or new_categoria is list[None]:
        raise statusMessage.NOT_DATA
    
    created = await Categoria_CRUD.createCategoria(new_categoria)
    
    if not created:
        raise statusMessage.NOT_SUCCESS
        
    
    res.status_code = status.HTTP_201_CREATED

@router_categoria.delete("/deleteOneCategoria{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if id is None or id < 1:
        raise statusMessage.NOT_DATA
    
    removed = await Categoria_CRUD.deleteCategoria(id)
    
    if not removed:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED