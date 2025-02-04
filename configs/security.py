from email.message import Message
from email.errors import MessageError

from smtplib import SMTP, SMTPException

from random import randint

from pwdlib import PasswordHash

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, WebSocket, WebSocketException

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import encode, decode
from jwt.exceptions import PyJWTError

from configs.settings import Config

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from model.Model_Conta import Conta

from configs.register import engine

pwd_context = PasswordHash.recommended()

SECRET_KEY = "segredo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES = 60 * 1.5

WAITING_USERS: dict[str, WebSocket] = {}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="conta/doLogin")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def getJWTToken(data: dict):
    try:
        to_encode = data.copy()

        expires_in = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRES
        )

        to_encode.update({"exp": expires_in})

        jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return jwt
    except ValueError as err:
        print(str(err))


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")

        if not user_email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Não foi possivel validar as credenciais",
            )
    except PyJWTError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possivel validar as credenciais",
        )

    try:
        with Session(engine) as session:
            user = (
                session.execute(select(Conta).where(Conta.email_conta == user_email))
                .scalars()
                .all()
            )

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Não foi possivel validar as credenciais",
                )

            return user

    except SQLAlchemyError as err:
        print(err._message())
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possivel validar as credenciais",
        )
    except Exception as err:
        print("Erro inesperado: {err}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possivel validar as credenciais",
        )


def gerar_codigo() -> str:
    codigo: str = ""
    
    maiusculas: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas: str = maiusculas.lower()
    caracter_especial: str = "!$%&#?"
    
    for i in range(0, 8):
        tipo_caracter: int = randint(0, 2)
        if tipo_caracter == 0:
            codigo += maiusculas[randint(0, len(maiusculas) - 1)]
        elif tipo_caracter == 1:
            codigo += minusculas[randint(0, len(minusculas) - 1)]
        else:
            codigo += caracter_especial[randint(0, len(caracter_especial) - 1)]
    
    return codigo

async def enviar_codigo_para_email(to_email: str, websocket: WebSocket) -> bool:
    try:
        codigo = gerar_codigo()
        
        expires_in = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
            minutes=10
        )
        
        token = encode({
            "code": codigo,
            "exp": expires_in
        }, SECRET_KEY, algorithm=ALGORITHM)
        
        link = f"{Config().DOMAIN}/conta/verify_token?token={token}&email={to_email}"
        
        corpo = f"""
            <img 
                src="https://static.wixstatic.com/media/640d45_d4ae64361f654cd9a73f8101f6d9b5e8~mv2_d_14815_6035_s_5_3_2.jpg/v1/fit/w_2500,h_1330,al_c/640d45_d4ae64361f654cd9a73f8101f6d9b5e8~mv2_d_14815_6035_s_5_3_2.jpg"
                alt="Colegio Mirim logo"
                style="width: 200px; margin: auto;"
            />
            <h1>Código para verificação de e-mail</h1>
            <p>Clique <a href={link}>aqui</a> para validar o email</p>
        """
        
        msg = Message()
        
        msg['Subject'] = "Verificação de conta"
        msg['From'] = "yuri.ferreira@colegiomirim.com.br"
        msg['To'] = to_email
        
        password = Config().EMAIL_PASS
        
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(corpo)
        
        smt = SMTP("smtp.gmail.com: 587")
        smt.starttls()
        
        smt.login(msg['From'], password)
        smt.sendmail(msg["From"], [msg['To']], msg.as_string().encode("utf-8"))
        
        print("email enviado")
        
        WAITING_USERS[to_email] = websocket
        result: dict[str, str] = await websocket.receive_json()
        print("chegou")
        if result["token"] == token and verify_token_email(result["token"]):
            print("email validado")
            return True
    except MessageError as err:
        print(err)
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Erro ao preparar o email"
        )
    except SMTPException as err:
        print(err)
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Erro ao enviar o email"
        )
    except WebSocketException as err:
        print(str(err))
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Erro ao preparar o email"
        )
        
async def validar_conta(email: str, token: str):
    try:
        if email in WAITING_USERS:
            await WAITING_USERS[email].send_json(data={
                "token": token,
                "email": email
            })
    except WebSocketException as err:
        print(str(err))
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Erro ao preparar o email"
        )

async def verify_token_email(token):
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        codigo = payload.get("code")
        if not codigo:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
            )
        return True
    except PyJWTError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
        )