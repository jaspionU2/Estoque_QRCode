from fastapi import APIRouter, Response, Depends, HTTPException, status, WebSocket, WebSocketException

from fastapi.responses import RedirectResponse, HTMLResponse

from fastapi.security import OAuth2PasswordRequestForm

from service.Conta_service import Conta_CRUD

from configs import statusMessage

from configs.settings import Config

from configs.security import verify_password, getJWTToken, enviar_codigo_para_email, validar_conta

from model.Model_Conta import Conta

from schema.Schema_Conta import SchemaConta, SchemaContaPublic

router_conta = APIRouter()  

@router_conta.get("/teste")
async def teste():
    return HTMLResponse("""
           <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>teste websocket</title>
</head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/conta/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>             
    """)
    
@router_conta.websocket("/ws")
async def web(websocket: WebSocket):
    print("ajhsb")
    try:
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            print(data)
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketException as err:
        return str(err)

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

@router_conta.get("/verify_token")
async def create_account_token(
    token: str,
    email: str
) -> dict:
    await validar_conta(email, token)
    return {
        "detail": "conta criada"
    }

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

@router_conta.post("/addNewConta", response_model=dict)
async def create(
    new_conta: SchemaConta,
    res: Response,
    websocket: WebSocket
) -> dict:
    
    
    if not new_conta:
        raise statusMessage.NOT_DATA
    
    new_conta = new_conta.model_copy(update={"email_conta": new_conta.email_conta})

    conta_dict = new_conta.model_dump()
    conta_dict["senha_conta"] = new_conta.senha_conta.get_secret_value()
    
    await websocket.accept()
    
    recived = await enviar_codigo_para_email(new_conta.email_conta, websocket)
    
    if recived:
        created = await Conta_CRUD.createConta(conta_dict)
        
        
        if not created:
            raise statusMessage.NOT_SUCCESS
        
        
            
        res.status_code = status.HTTP_201_CREATED
        return {
            "detail": f"Email de verificação enviado para {new_conta.email_conta}",
            "data": created
        }
        
    return {
        "detail": "houve algum erro"
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