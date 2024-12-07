from fastapi import APIRouter, Response, status  

router_categoria = APIRouter()  

@router_categoria.get("/getAllCategorias")
async def get(res: Response) -> list:
    categorias = [""] # service.getAllCategorias()
    return categorias

@router_categoria.post("/addNewCategoria")
async def create(new_categoria: dict, res: Response) -> None:
    if new_categoria == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.createNewCategoria(new_categoria.value)

@router_categoria.delete("/deleteOneCategoria")
async def delete(categoria: dict, res: Response) -> None:
    if categoria == None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return None
    
    # service.deleteCategoria(categoria.value)