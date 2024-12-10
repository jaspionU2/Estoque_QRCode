from fastapi import APIRouter, Response, status  
from services.Categorias_service import Categoria_CRUD

router_categoria = APIRouter()  

@router_categoria.get("/getAllCategorias")
async def get(res: Response) -> list:
    categorias = await Categoria_CRUD.getAllCategorias()
    return categorias

@router_categoria.post("/addNewCategoria")
async def create(new_categoria: list[dict], res: Response) -> None:
    if new_categoria == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    if await Categoria_CRUD.createCategoria(new_categoria) < 1:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

@router_categoria.delete("/deleteOneCategoria{id}")
async def delete(id: int, res: Response) -> None:
    if id == None and id < 1:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    await Categoria_CRUD.deleteCategoria(id)