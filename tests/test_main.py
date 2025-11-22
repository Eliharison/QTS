from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_buscar_estudante_por_id():
    response = client.get("estudante/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nome": "Eliharison",
        "idade": 20
    }


def test_buscar_estudante_por_id_inexistente():
    response = client.get("estudante/999")
    assert response.status_code == 404
    assert response.json() == {
        "detail": {
            "mensagem": "Estudante não encontrado"
        }
    }