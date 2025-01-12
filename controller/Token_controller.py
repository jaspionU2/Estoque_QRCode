from fastapi import APIRouter, Response, status, Depends, HTTPException

from fastapi.security import OAuth2PasswordRequestForm

from services.Conta_service import Conta_CRUD

from configs.security import verify_password, getJWTToken

from configs.statusMessage import messages

router_token = APIRouter()  

@router_token.post('/token')
async def getToken(form_data: OAuth2PasswordRequestForm = Depends()):
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
