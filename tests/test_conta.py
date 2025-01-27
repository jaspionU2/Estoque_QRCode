from fastapi.testclient import TestClient

from http import HTTPStatus

from model.Model_Conta import Conta
from index import app

client = TestClient(app)

def test_getAllUsers_retorna_users():    
    response = client.get('/conta/getAllContas')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json()
    
def test_doLogin_return_token():
    res = client.post("/conta/doLogin", data={
        "username": "yurigabriel.f1012@gmail.com",
        "password": "Yuri1234$"
    })
    
    assert res.status_code == HTTPStatus.OK
    assert res.json()
    
def test_doLogin_erro():
    res = client.post("/conta/doLogin", data={
        "username": "yurigabriel1012@gmail.com",
        "password": "Yuri1234$"
    })
    
    assert res.status_code == HTTPStatus.BAD_REQUEST
    assert res.json()