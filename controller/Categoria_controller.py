from fastapi import APIRouter, Response, status  
from services.Categorias_service import Categoria_CRUD

from model.Model_Categoria import Categoria

router_categoria = APIRouter()  

@router_categoria.get("/getAllCategorias")
async def get(res: Response) -> list[Categoria]:
    categorias = await Categoria_CRUD.getAllCategorias()
    if categorias is None:
        res.status_code = status.HTTP_404_NOT_FOUND
        return None
    
    res.status_code = status.HTTP_200_OK
    return categorias

@router_categoria.post("/addNewCategoria")
async def create(new_categoria: list[Categoria], res: Response) -> dict:
    if new_categoria is None or new_categoria is list[None]:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": "Ausencia de dados",
            "created": False
        }
    
    created = await Categoria_CRUD.createCategoria(new_categoria)
    
    if not created:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "created": False
        }
        
    
    res.status_code = status.HTTP_201_CREATED
    return {
        "created": True
    }

@router_categoria.delete("/deleteOneCategoria{id}")
async def delete(id: int, res: Response) -> dict:
    if id is None or id < 1:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": "Ausencia de dados",
            "removed": False
        }
    
    removed = await Categoria_CRUD.deleteCategoria(id)
    
    if not removed:
        res.status_code = status.HTTP_400_BAD_REQUEST
    
    res.status_code = status.HTTP_202_ACCEPTED