from main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_read_user():
    response = client.get("/fast/user")
    assert response.status_code == 200
    assert response.json()






