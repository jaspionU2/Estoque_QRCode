from fastapi import APIRouter, Response, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm

from service.Conta_service import Conta_CRUD

from configs import statusMessage

from configs.security import verify_password, getJWTToken

from model.Model_Conta import Conta

from schema.Schema_Conta import SchemaConta, SchemaContaPublic

router_conta = APIRouter()  

@router_conta.post("/doLogin")
async def login(
    res: Response,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    result_conta = await Conta_CRUD.getOneConta(form_data.username)
    
    if not result_conta or not verify_password(form_data.password, result_conta["senha_conta"]):
        raise HTTPException (
            status_code=400,
            detail="Incorrect email or password"
        )
    
    token = getJWTToken(data={"sub": result_conta["email_conta"]})
    
    res.status_code = status.HTTP_200_OK
    return {
        "access_token": token,
        "type_token": "Bearer"
    }

@router_conta.get("/getAllContas")
async def get(
    res: Response
) -> list[Conta]:
    result_conta = await Conta_CRUD.getAllConta()
    
    if result_conta is None or result_conta is []:
        raise statusMessage.NOT_FOUND

    res.status_code = status.HTTP_200_OK
    return result_conta

@router_conta.post("/addNewConta", response_model=SchemaContaPublic)
async def create(
    new_conta: SchemaConta,
    res: Response
) -> SchemaContaPublic:
    
    if not new_conta:
        raise statusMessage.NOT_DATA
    
    conta_dict = new_conta.model_dump()
    conta_dict["senha_conta"] = new_conta.senha_conta.get_secret_value()
    
    result_conta = await Conta_CRUD.createConta(conta_dict)
    
    if not result_conta:
        raise statusMessage.NOT_SUCCESS
        
    res.status_code = status.HTTP_201_CREATED
    return result_conta

@router_conta.put("/updateConta/{id}", response_model=SchemaContaPublic)
async def update(
    id: int,
    new_values: SchemaConta,
    res: Response
) -> SchemaContaPublic:
    
    if not new_values:
        raise statusMessage.NOT_DATA
    
    conta_dict = new_values.model_dump()
    conta_dict["senha_conta"] = new_values.senha_conta.get_secret_value()    
    
    result_conta = await Conta_CRUD.updateConta(id, conta_dict)
    
    if not result_conta:
        raise statusMessage.NOT_FOUND
    
    res.status_code  = status.HTTP_202_ACCEPTED
    
    return result_conta

@router_conta.delete("/deleteConta/{id}")
async def delete(
    id: int,
    res: Response
) -> None:
    if id is None or id < 1:
        raise statusMessage.NOT_DATA
    
    removed = await Conta_CRUD.deleteConta(id)
    
    if not removed:
        raise statusMessage.NOT_SUCCESS
    
    res.status_code = status.HTTP_202_ACCEPTED