# tests/test_login.py

import requests
import pytest

from api.auth import login


def test_login_success_sets_authorization2_cookie(config):
    session = requests.Session()
    login(session, config.base_url, config.email, config.password)

    assert session.cookies.get("Authorization2"), "Authorization2 cookie was not set"


def test_login_invalid_password_fails(config):
    session = requests.Session()

    with pytest.raises(AssertionError):
        login(session, config.base_url, config.email, "WrongPassword123!")