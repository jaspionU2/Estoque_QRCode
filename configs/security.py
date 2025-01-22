from pwdlib import PasswordHash

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

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
ACCESS_TOKEN_EXPIRES = 60

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
