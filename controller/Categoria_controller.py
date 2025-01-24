from fastapi import APIRouter, Response, status, Depends 
from service.Categorias_service import Categoria_CRUD

from configs import statusMessage
from configs.security import get_current_user

from schema.Schema_Status_Categoria_Serie_Materia import SchemaCategoria, SchemaCategoriaPublico

router_categoria = APIRouter()  

@router_categoria.get("/getAllCategorias")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    
    result_categoria = await Categoria_CRUD.getAllCategorias()
    
    if result_categoria is None or result_categoria is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return result_categoria

@router_categoria.post("/addNewCategoria", response_model=SchemaCategoriaPublico)
async def create(
    new_categoria: SchemaCategoria,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaCategoriaPublico:
    
    if new_categoria is None or new_categoria is list[None]:
        raise statusMessage.NOT_DATA
    
    result_categoria = await Categoria_CRUD.createCategoria(new_categoria.model_dump())
    
    if not result_categoria:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_201_CREATED
    return result_categoria

@router_categoria.delete("/deleteOneCategoria/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    if id is None or id < 1:
        raise statusMessage.NOT_DATA
    
    result_removed = await Categoria_CRUD.deleteCategoria(id)
    
    if not result_removed:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED