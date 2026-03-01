# api/auth.py

import requests


LOGIN_PATH = "/api/v0.0.2/login"


def login(session: requests.Session, base_url: str, email: str, password: str) -> None:
    """
    Performs login using the same endpoint as the web UI.
    On success, the server sets the 'Authorization2' cookie.
    """

    url = f"{base_url}{LOGIN_PATH}"
    payload = {
        "email": email,
        "password": password,
    }

    response = session.post(url, json=payload, headers={"Accept": "application/json"})

    # Basic status validation
    if response.status_code != 200:
        raise AssertionError(
            f"Login failed with status {response.status_code}: {response.text}"
        )

    # Verify that authentication cookie was set
    auth_cookie = session.cookies.get("Authorization2")
    if not auth_cookie:
        raise AssertionError(
            "Login did not set Authorization2 cookie. "
            f"Response headers: {response.headers}"
        )