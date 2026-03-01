# tests/test_deals_list.py

from api.deals import get_deals_list


def test_deals_list_contains_exactly_one_expected_deal(api_session, config):
    result = get_deals_list(api_session, config.base_url, config.deals_view)

    assert result.get("message") == "Successful", f"Unexpected response: {result}"

    deals = result.get("data")
    assert isinstance(deals, list), f"Expected 'data' list, got: {type(deals)}"
    assert len(deals) == 1, f"Expected exactly 1 deal, got {len(deals)}: {deals}"

    deal = deals[0]
    assert deal.get("title") == config.expected_deal_title, (
        f"Expected deal title '{config.expected_deal_title}', got '{deal.get('title')}'. "
        f"Deal: {deal}"
    )