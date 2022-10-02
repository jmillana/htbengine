"""Token API endpoints."""
import requests

from htbengine.api.endpoints import HTB_BASE_URL


def get_api_token(user: str, password: str) -> str:
    """Get the API token from HTB.

    Connect to HTB with the user and password and get the API token

    Returns:
        str: The API token
    """
    headers = {
        "User-Agent": "htbengine",
        "Content-Type": "application/json; charset=utf-8",
    }
    data = {"email": user, "password": password, "remember": True}
    r = requests.post(
        HTB_BASE_URL + "/login", headers=headers, json=data, timeout=20
    )
    return r.json()["message"]["access_token"]
