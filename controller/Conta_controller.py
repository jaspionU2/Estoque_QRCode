from fastapi import APIRouter, Response, Depends, HTTPException, status

from fastapi.responses import RedirectResponse

from fastapi.security import OAuth2PasswordRequestForm

from service.Conta_service import Conta_CRUD

from configs import statusMessage

from configs.settings import Config

from configs.security import verify_password, getJWTToken, enviar_codigo_para_email, verify_token_email

from model.Model_Conta import Conta

from schema.Schema_Conta import SchemaConta, SchemaContaPublic, AddNewContaReturnStm
from schema.Schema_token import TokenPublic

router_conta = APIRouter()  

@router_conta.post("/doLogin", status_code=status.HTTP_200_OK, response_model=TokenPublic)
async def login(
    res: Response,
    form_data: OAuth2PasswordRequestForm = Depends()
) -> TokenPublic:
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
async def get(
    res: Response
) -> list[Conta]:
    contas = await Conta_CRUD.getAllConta()
    
    if contas is None or contas is []:
        raise statusMessage.NOT_FOUND

    res.status_code = status.HTTP_200_OK
    return contas

@router_conta.get("/verify_token")
async def create_account_token(
    token: str,
    email: str
):
    
    is_valid_token = verify_token_email(token)
    
    if is_valid_token:
        if not email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email inválido"
            )
        
        updated = await Conta_CRUD.turn_verifed_account(email)
        
        if not updated:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Erro ao verificar a conta"
            )
            
        return RedirectResponse(
            url=Config().VERIFY_ACCOUNT_PAGE_ROUTE,
            headers={
                "verifed": True
            }
        )
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Erro ao validar o token"
    )

@router_conta.delete("/delete_accounts_not_verified", response_model=dict)
async def delete_accounts_not_verified() -> dict:
    deleted = await Conta_CRUD.delete_accounts_not_verifed()
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu algum erro ao deletar as contas"
        )
    
    return {
        "detail": "Contas deletadas"
    }

@router_conta.post("/addNewConta", status_code=status.HTTP_201_CREATED, response_model=AddNewContaReturnStm)
async def create(
    new_conta: SchemaConta,
    res: Response
) -> AddNewContaReturnStm:
    
    if not new_conta:
        raise statusMessage.NOT_DATA
    
    new_conta = new_conta.model_copy(update={"email_conta": new_conta.email_conta})

    conta_dict = new_conta.model_dump()
    conta_dict["senha_conta"] = new_conta.senha_conta.get_secret_value()
    
    result = await Conta_CRUD.createConta(conta_dict)
    
    
    if not result:
        raise statusMessage.NOT_SUCCESS
    
    enviar_codigo_para_email(new_conta.email_conta)
        
    res.status_code = status.HTTP_201_CREATED
    return {
        "detail": f"Email de verificação enviado para {new_conta.email_conta}",
        "data": result
    }

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
    
    result = await Conta_CRUD.updateConta(id, conta_dict)
    
    if not result:
        raise statusMessage.NOT_FOUND
    
    res.status_code  = status.HTTP_202_ACCEPTED
    
    return result

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