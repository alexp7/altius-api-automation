from dataclasses import dataclass
import os
from dotenv import load_dotenv


@dataclass(frozen=True)
class Config:
    base_url: str
    email: str
    password: str
    deals_view: str
    expected_deal_title: str


def load_config() -> Config:
    load_dotenv()

    base_url = os.getenv("BASE_URL")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    deals_view = os.getenv("DEALS_VIEW", "task-manage")
    expected_deal_title = os.getenv("EXPECTED_DEAL_TITLE", "INTC")

    if not base_url or not email or not password:
        raise RuntimeError("Missing required environment variables.")

    return Config(
        base_url=base_url.rstrip("/"),
        email=email,
        password=password,
        deals_view=deals_view,
        expected_deal_title=expected_deal_title,
    )