from typing import Union
from requests import Response

import requests


class HTTP:
    def __init__(self):
        pass

    @staticmethod
    def request(
            url: str,
            headers: dict,
            params: dict,
            method: str,
    ) -> Union[Response, None]:
        response = getattr(requests, method.lower())(
            url, params=params, headers=headers
        )

        return response
