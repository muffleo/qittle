from qittle.types import (
    HookDescription,
    Response,
)

from .api import API


def register_hook(api: API, server: str) -> HookDescription:
    response = api.request(
        "PUT /payment-notifier/v1/hooks",
        hookType=1, param=server, txnType=2
    )

    return HookDescription(**response)


def get_hook(api: API) -> HookDescription:
    response = api.request(
        "GET /payment-notifier/v1/hooks/active",
    )

    return HookDescription(**response)


def delete_hook(api: API, hid: str) -> Response:
    response = api.request(
        f"DELETE /payment-notifier/v1/hooks/{hid}",
    )

    return Response(**response)


def trigger_hook(api: API) -> Response:
    response = api.request(
        "GET /payment-notifier/v1/hooks/test",
    )

    return Response(**response)
