import openai
from unittest.mock import patch

# Reuse the authentication fixture defined in test_auth so we can
# obtain a valid JWT for authorized requests.
# Import fixtures from the auth test module so they are available here.
from backend.tests.test_auth import auth_token  # noqa: F401
from backend.tests.test_auth import test_user_data  # noqa: F401


def test_agent_chat_success(test_client, auth_token):
    """Agent returns successful response when OpenAI call succeeds."""
    with patch("backend.routers.agent.openai.ChatCompletion.create") as mock_create, \
         patch("backend.routers.agent.openai.api_key", "test-key"):
        mock_create.return_value = {
            "choices": [{"message": {"content": "Stay strong."}}]
        }
        response = test_client.post(
            "/agent/chat",
            json={"message": "Hello"},
            headers={"Authorization": f"Bearer {auth_token}"},
        )

    assert response.status_code == 200
    assert response.json()["response"] == "Stay strong."


def test_agent_chat_requires_auth(test_client):
    """Endpoint should reject requests without authentication."""
    response = test_client.post("/agent/chat", json={"message": "Hi"})
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]


def test_agent_chat_invalid_token(test_client):
    """Endpoint should reject invalid JWT tokens."""
    response = test_client.post(
        "/agent/chat",
        json={"message": "Hi"},
        headers={"Authorization": "Bearer invalid"},
    )
    assert response.status_code == 401
    assert "Could not validate credentials" in response.json()["detail"]


def test_agent_chat_missing_message(test_client, auth_token):
    """Validation should fail when the message field is missing."""
    response = test_client.post(
        "/agent/chat",
        json={},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 422


def test_agent_chat_openai_failure(test_client, auth_token):
    """Server returns 500 when OpenAI raises an error."""
    with patch(
        "backend.routers.agent.openai.ChatCompletion.create",
        side_effect=openai.OpenAIError("oops"),
    ), patch("backend.routers.agent.openai.api_key", "test-key"):
        response = test_client.post(
            "/agent/chat",
            json={"message": "Hi"},
            headers={"Authorization": f"Bearer {auth_token}"},
        )

    assert response.status_code == 500
    assert "Agent error" in response.json()["detail"]
