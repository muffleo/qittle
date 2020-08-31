from qittle.types import Key
from .api import API


def get_key(api: API, hid: str) -> Key:
    response = api.request(
        f"GET /payment-notifier/v1/hooks/{hid}/key",
    )

    return Key(**response)


def change_key(api: API, hid: str) -> Key:
    response = api.request(
        f"POST /payment-notifier/v1/hooks/{hid}/newkey",
    )

    return Key(**response)
