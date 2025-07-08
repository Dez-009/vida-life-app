import pytest
from backend.models.user import Base

@pytest.fixture
def test_user_data():
    return {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpass123"
    }

@pytest.fixture
def registered_user(test_client, test_user_data):
    response = test_client.post("/register", json=test_user_data)
    return response.json()

@pytest.fixture
def auth_token(test_client, test_user_data):
    test_client.post("/register", json=test_user_data)
    response = test_client.post(
        "/token",
        data={
            "username": test_user_data["email"],
            "password": test_user_data["password"]
        }
    )
    return response.json()["access_token"]

def test_register_user_success(test_client, test_user_data):
    response = test_client.post("/register", json=test_user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user_data["email"]
    assert data["username"] == test_user_data["username"]
    assert "id" in data
    assert data["is_active"] is True

def test_register_user_duplicate_email(test_client, registered_user, test_user_data):
    response = test_client.post("/register", json=test_user_data)
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]

def test_register_user_invalid_email(test_client):
    response = test_client.post(
        "/register",
        json={
            "email": "invalid-email",
            "username": "testuser",
            "password": "testpass123"
        }
    )
    assert response.status_code == 422  # Validation error

def test_register_user_missing_fields(test_client):
    response = test_client.post(
        "/register",
        json={
            "email": "test@example.com"
        }
    )
    assert response.status_code == 422

def test_login_success(test_client, registered_user, test_user_data):
    response = test_client.post(
        "/token",
        data={
            "username": test_user_data["email"],
            "password": test_user_data["password"]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(test_client, registered_user, test_user_data):
    response = test_client.post(
        "/token",
        data={
            "username": test_user_data["email"],
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401
    assert "Incorrect email or password" in response.json()["detail"]

def test_login_nonexistent_user(test_client):
    response = test_client.post(
        "/token",
        data={
            "username": "nonexistent@example.com",
            "password": "testpass123"
        }
    )
    assert response.status_code == 401

def test_get_user_me_success(test_client, auth_token):
    response = test_client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert "username" in data
    assert "id" in data

def test_get_user_me_no_token(test_client):
    response = test_client.get("/users/me")
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]

def test_get_user_me_invalid_token(test_client):
    response = test_client.get(
        "/users/me",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401
    assert "Could not validate credentials" in response.json()["detail"]

def test_update_profile_success(test_client, auth_token):
    profile_data = {
        "full_name": "Test User",
        "age": 30,
        "date_of_birth": "1995-01-01",
        "address": "123 Test St",
        "phone": "1234567890",
        "is_married": True,
        "annual_income": 75000,
        "number_of_children": 2,
        "sex": "male"
    }
    
    response = test_client.put(
        "/users/me/profile",
        json=profile_data,
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    for key, value in profile_data.items():
        if key == 'annual_income':
            assert float(data[key]) == float(value)
        else:
            assert data[key] == value

def test_update_profile_invalid_data(test_client, auth_token):
    invalid_data = {
        "age": "invalid_age",  # Should be integer
        "date_of_birth": "invalid_date",  # Should be YYYY-MM-DD
        "annual_income": "invalid_income"  # Should be number
    }
    
    response = test_client.put(
        "/users/me/profile",
        json=invalid_data,
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 422

def test_update_profile_partial(test_client, auth_token):
    # Update only some fields
    partial_data = {
        "full_name": "Updated Name",
        "age": 31
    }
    
    response = test_client.put(
        "/users/me/profile",
        json=partial_data,
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == partial_data["full_name"]
    assert data["age"] == partial_data["age"]
    # Other fields should remain unchanged
    assert "email" in data
    assert "username" in data

def test_update_profile_no_auth(test_client):
    response = test_client.put(
        "/users/me/profile",
        json={"full_name": "Test User"}
    )
    assert response.status_code == 401
