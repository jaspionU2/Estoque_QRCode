from fastapi import APIRouter, Response, status, Depends, HTTPException
from service.Materia_service import Materia_CRUD  

from configs import statusMessage
from configs.security import get_current_user
from configs.CustomResponse import CustomResponse

from schema.Schema_Status_Categoria_Serie_Materia import SchemaMateria, SchemaMateriaPublico

router_materia = APIRouter()  

@router_materia.get("/getAllMaterias")
async def get(
    res: Response,
    current_user = Depends(get_current_user)
) -> list:
    
    result_materia = Materia_CRUD.getAllMaterias()
    
    if result_materia is None or result_materia is []:
        raise statusMessage.NOT_FOUND
    
    res.status_code = status.HTTP_200_OK
    return result_materia

@router_materia.post("/addNewMateria", response_model=SchemaMateriaPublico)
async def create(
    new_materia: SchemaMateria ,
    res: Response,
    current_user = Depends(get_current_user)
) -> SchemaMateriaPublico:
    
    if new_materia is None or new_materia is []:
        raise statusMessage.NOT_DATA
    
    result_materia = Materia_CRUD.createMateria(new_materia.model_dump())
    
    if isinstance(result_materia, CustomResponse):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=result_materia.to_dict()
        )
    
    if not result_materia:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_201_CREATED
    return result_materia

@router_materia.delete("/deleteOneMateria/{id}")
async def delete(
    id: int,
    res: Response,
    current_user = Depends(get_current_user)
) -> None:
    
    if id == None and id <= 0:
        raise statusMessage.NOT_DATA
    
    result_materia = Materia_CRUD.deleteMateria(id)
    
    if isinstance(result_materia, CustomResponse):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=result_materia.to_dict()
        )
    
    res.status_code = status.HTTP_202_ACCEPTED