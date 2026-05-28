from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_organization_returns_201() -> None:
    post_response = client.post("/organizations", json={"name": "Acme Inc"})

    assert post_response.status_code == 201
    data = post_response.json()
    assert "id" in data
    assert data.get("name") == "Acme Inc"


def test_get_organization_after_creation() -> None:
    post_response = client.post("/organizations", json={"name": "Acme Inc"})
    org_id = post_response.json().get("id")

    get_response = client.get(f"/organizations/{org_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data.get("name") == "Acme Inc"


def test_get_invalid_organization_id_returns_404() -> None:
    get_response = client.get("/organizations/bad_id")
    assert get_response.status_code == 404
    data = get_response.json()
    assert data == {"detail": "Organization with id: bad_id not found"}


def test_create_organization_with_invalid_payload() -> None:
    post_response = client.post("/organizations", json={"Name": "Acme Inc"})
    assert post_response.status_code == 422
