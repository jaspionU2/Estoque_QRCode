from fastapi import APIRouter, Response, status, Depends, HTTPException

from fastapi.security import OAuth2PasswordRequestForm

from services.Conta_service import Conta_CRUD

from configs.statusMessage import messages

from configs.security import verify_password, getJWTToken

from model.Model_Conta import Conta

router_conta = APIRouter()  

@router_conta.post("/doLogin")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conta = await Conta_CRUD.getOneConta(form_data.username)
    
    if not conta or not verify_password(form_data.password, conta["senha_conta"]):
        raise HTTPException (
            status_code=400,
            detail="Incorrect email or password"
        )
    
    token = getJWTToken(data={"sub": conta["email_conta"]})
    
    return {
        "access_token": token,
        "type_token": "Bearer"
    }

@router_conta.get("/getAllContas")
async def get(res: Response) -> list[Conta]:
    contas = await Conta_CRUD.getAllConta()
    print(contas)
    if contas is None or contas is []:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [messages["getErro"]]
    
    res.status_code = status.HTTP_200_OK
    return contas

@router_conta.post("/addNewConta")
async def create(new_conta: Conta, res: Response):
    if new_conta is None:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    conta = await Conta_CRUD.createConta(new_conta)
    
    if conta is None:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
        
    
    res.status_code = status.HTTP_201_CREATED
    return conta

@router_conta.put("/updateConta/{id}")
async def update(id: int, new_values: dict, res: Response) -> dict:
    if not new_values:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    result = await Conta_CRUD.updateConta(id, new_values)
    
    if not result:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code  = status.HTTP_200_OK
    return messages["sucess"]

@router_conta.delete("/deleteConta{id}")
async def delete(id: int, res: Response) -> dict:
    if id is None or id < 1:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return messages["not_data"]
    
    removed = await Conta_CRUD.deleteConta(id)
    
    if not removed:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return messages["not_sucess"]
    
    res.status_code = status.HTTP_200_OK
    return messages["sucess"]