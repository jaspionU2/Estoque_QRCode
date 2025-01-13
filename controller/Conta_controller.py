from fastapi import APIRouter, Response, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm

from services.Conta_service import Conta_CRUD

from configs import statusMessage

from configs.security import verify_password, getJWTToken

from model.Model_Conta import Conta

router_conta = APIRouter()  

@router_conta.post("/doLogin")
async def login(
    res: Response,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    conta = await Conta_CRUD.getOneConta(form_data.username)
    
    if not conta or not verify_password(form_data.password, conta["senha_conta"]):
        raise HTTPException (
            status_code=400,
            detail="Incorrect email or password"
        )
    
    token = getJWTToken(data={"sub": conta["email_conta"]})
    
    res.status_code = status.HTTP_200_OK
    return {
        "access_token": token,
        "type_token": "Bearer"
    }

@router_conta.get("/getAllContas")
async def get(
    res: Response
) -> list[Conta]:
    contas = await Conta_CRUD.getAllConta()
    
    if contas is None or contas is []:
        raise statusMessage.NOT_FOUND

    res.status_code = status.HTTP_200_OK
    return contas

@router_conta.post("/addNewConta")
async def create(
    new_conta: Conta,
    res: Response
) -> dict:
    if not new_conta:
        raise statusMessage.NOT_DATA
    
    created = await Conta_CRUD.createConta(new_conta)
    
    if not created:
        raise statusMessage.NOT_SUCCESS
        
    
    res.status_code = status.HTTP_201_CREATED
    return new_conta.__dict__

@router_conta.put("/updateConta/{id}")
async def update(
    id: int,
    new_values: dict,
    res: Response
) -> None:
    if not new_values:
        raise statusMessage.NOT_DATA
    
    result = await Conta_CRUD.updateConta(id, new_values)
    
    if not result:
        raise statusMessage.NOT_FOUND
    
    res.status_code  = status.HTTP_202_ACCEPTED

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