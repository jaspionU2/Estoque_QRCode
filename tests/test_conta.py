from fastapi.testclient import TestClient

from http import HTTPStatus

from model.Model_Conta import Conta

from schema.Schema_token import TokenPublic
from schema.Schema_Conta import AddNewContaReturnStm

from index import app

client = TestClient(app)

def test_getAllContas_return_users():    
    response = client.get('/conta/getAllContas')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json()
    
def test_doLogin_return_token():
    res = client.post("/conta/doLogin", data={
        "username": "yurigabriel.f1012@gmail.com",
        "password": "Yuri1234$"
    })
    
    assert res.status_code == HTTPStatus.OK
    
    try:
        token_data = TokenPublic(**res.json())
        assert token_data.type_token == "Bearer"
    except Exception as e:
        assert False, f"Resposta inválida: {e}"
    
def test_doLogin_erro():
    res = client.post("/conta/doLogin", data={
        "username": "yurigabriel1012@gmail.com",
        "password": "Yuri1234$"
    })
    
    assert res.status_code == HTTPStatus.BAD_REQUEST
    assert res.json()
    
def test_addNewConta_return_data():
    
    user = "Teste"
    email = "teste@gmail.com"
    password = "Teste123$"
    
    res = client.post("/conta/addNewConta", json={
        "usuario_conta": user,
        "email_conta": email,
        "senha_conta": password
    })
    
    assert res.status_code == HTTPStatus.CREATED
    
    try:
        res_data = AddNewContaReturnStm(**res.json())
        assert res_data.detail == f"Email de verificação enviado para {email}"
    except Exception as err:
        assert False, f"Resposta inválida: {err}"
    