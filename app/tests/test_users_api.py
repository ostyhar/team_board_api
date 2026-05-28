from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_user_returns_201() -> None:
    response = client.post(
        "/users", json={"email": "alex@example.com", "display_name": "Alex"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data.get("email") == "alex@example.com"
    assert data.get("display_name") == "Alex"


def test_get_created_user() -> None:
    post_response = client.post(
        "/users", json={"email": "anna@example.com", "display_name": "Anna"}
    )

    user_id = post_response.json().get("id")
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data.get("email") == "anna@example.com"
    assert data.get("display_name") == "Anna"


def test_get_unknown_user() -> None:
    get_response = client.get("/users/bad_id")
    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "user with id: bad_id not found"}


def test_invalid_user_payload() -> None:
    post_response = client.post("/users", json={"email": "anna@example.com"})
    assert post_response.status_code == 422


def test_duplicate_user() -> None:
    payload = {"email": "anna@example.com", "display_name": "Anna"}
    post_response_1 = client.post("/users", json=payload)
    post_response_2 = client.post("/users", json=payload)

    assert post_response_1.status_code == 201
    assert post_response_2.status_code == 409
    assert post_response_2.json() == {"detail": "anna@example.com already exists"}
