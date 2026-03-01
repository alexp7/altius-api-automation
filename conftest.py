# conftest.py

import pytest
import requests

from utils.config import load_config
from api.auth import login


@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="session")
def api_session(config):
    session = requests.Session()
    login(session, config.base_url, config.email, config.password)
    return session