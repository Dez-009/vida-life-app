import pytest
from unittest.mock import patch, MagicMock


def build_openai_response(content: str):
    """Helper to construct a fake OpenAI completion object."""
    mock_choice = MagicMock()
    mock_choice.message.content = content
    return MagicMock(choices=[mock_choice])


def auth_header(token: str):
    """Create Authorization header for Bearer tokens."""
    return {"Authorization": f"Bearer {token}"}


@patch("routers.agent.client.chat.completions.create")
def test_agent_chat_success(mock_create, test_client, auth_token):
    """Successful chat should return the mocked response."""
    mock_create.return_value = build_openai_response("Stay strong.")

    response = test_client.post(
        "/agent/chat",
        json={"message": "How are you?"},
        headers=auth_header(auth_token),
    )

    assert response.status_code == 200
    assert response.json()["response"] == "Stay strong."


def test_agent_chat_requires_auth(test_client):
    """Request without token should fail."""
    response = test_client.post("/agent/chat", json={"message": "Hello"})

    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]


def test_agent_chat_invalid_token(test_client):
    """Invalid token should be rejected."""
    response = test_client.post(
        "/agent/chat",
        json={"message": "Hi"},
        headers=auth_header("badtoken"),
    )

    assert response.status_code == 401
    assert "Could not validate credentials" in response.json()["detail"]


@patch("routers.agent.client.chat.completions.create")
def test_agent_chat_missing_message(mock_create, test_client, auth_token):
    """Missing message field triggers validation error."""
    response = test_client.post(
        "/agent/chat",
        json={},
        headers=auth_header(auth_token),
    )

    assert response.status_code == 422


@patch("routers.agent.client.chat.completions.create", side_effect=Exception("boom"))
def test_agent_chat_openai_failure(mock_create, test_client, auth_token):
    """OpenAI errors should return a 500 Agent error."""
    response = test_client.post(
        "/agent/chat",
        json={"message": "Advise me"},
        headers=auth_header(auth_token),
    )

    assert response.status_code == 500
    assert "Agent error" in response.json()["detail"]
