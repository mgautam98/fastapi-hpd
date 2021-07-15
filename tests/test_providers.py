from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_all_providers():
    response = client.get("/api/provider")
    assert response.status_code == 200
    # assert response.json == []


def test_get_a_provider():
    response = client.get("/api/provider/0f5b5b1d-08e0-4a32-9956-fb9b85cfdb2b")
    assert response.status_code == 200


def test_provider_not_exists():
    response = client.get("/api/provider/0f5b5b1d-08e0-4a32-9956-fb9b85cadb2b")
    assert response.status_code == 404


def test_create_a_provider():
    pass


def test_update_a_provider():
    pass


def test_delete_a_provider():
    pass
