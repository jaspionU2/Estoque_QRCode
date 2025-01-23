from fastapi.testclient import TestClient

from http import HTTPStatus

from model.Model_Conta import Conta
from index import app

def test_getAllUsers_retorna_users():
    client = TestClient(app)
    
    response = client.get('/conta/getAllContas')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json()