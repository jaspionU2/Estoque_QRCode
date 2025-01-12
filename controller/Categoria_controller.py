from fastapi import APIRouter, Response, status, Depends 
from services.Categorias_service import Categoria_CRUD

from configs.statusMessage import messages
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
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return categorias

@router_categoria.post("/addNewCategoria")
async def create(
    new_categoria: list[Categoria],
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if new_categoria is None or new_categoria is list[None]:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    created = await Categoria_CRUD.createCategoria(new_categoria)
    
    if not created:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
        
    
    res.status_code = status.HTTP_201_CREATED
    return messages["sucess"]

@router_categoria.delete("/deleteOneCategoria{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> dict:
    if id is None or id < 1:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    removed = await Categoria_CRUD.deleteCategoria(id)
    
    if not removed:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]