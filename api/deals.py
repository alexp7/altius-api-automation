# api/deals.py

import requests

DEALS_LIST_PATH = "/api/v0.0.2/deals-list"


def get_deals_list(session: requests.Session, base_url: str, view: str) -> dict:
    """
    Calls the deals-list endpoint.
    UI sends payload: {"view": "task-manage"}
    Returns parsed JSON response.
    """
    url = f"{base_url}{DEALS_LIST_PATH}"
    payload = {"view": view}

    response = session.post(url, json=payload, headers={"Accept": "application/json"})

    if response.status_code != 200:
        raise AssertionError(
            f"deals-list failed with status {response.status_code}: {response.text}"
        )

    try:
        return response.json()
    except Exception as e:
        raise AssertionError(f"deals-list returned non-JSON response: {e}")