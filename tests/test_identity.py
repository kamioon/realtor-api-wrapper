from unittest.mock import patch, Mock

from realtor_api_wrapper.identity.client import Client


def test_get_token():
    grant_type = "client_credentials"
    client_id = "test"
    client_secret = "test"
    scope = "DDFApi_Read"
    mock_patcher = patch("realtor_api_wrapper.identity.client.requests.post")
    success_login = {
        "access_token": "random_access_token_just_for_test",
        "expires_in": 3600,
        "token_type": "Bearer",
        "scope": "DDFApi_Read"
    }

    mock_client = mock_patcher.start()
    mock_client.return_value = Mock()
    mock_client.return_value.ok = True
    mock_client.return_value.json.return_value = success_login

    response = Client(client_id, client_secret).get_token(grant_type, scope)
    assert isinstance(response, dict)
    assert response['access_token'] is not None
    assert isinstance(response['expires_in'], int)
    assert response['expires_in'] >= 3600
    assert response['token_type'] == "Bearer"
    assert response['scope'] == "DDFApi_Read"
    assert response['access_token'] == success_login.get('access_token')
