from http import HTTPStatus
from qittle.http import HTTP
from qittle.utils import QiwiError


class API:
    def __init__(self, token: str) -> None:
        self.token = token

        self.http = HTTP()
        self._url = "https://edge.qiwi.com/"

    def request(self, method: str, **params) -> dict:
        request_method, api_path = method.split()

        response = self.http.request(
            url=self._url + api_path,
            params=params,
            method=request_method,
            headers={"Authorization": f"Bearer {self.token}"},
        )

        if response.status_code != 200:
            raise QiwiError(f"Abnormal status code: {response.status_code}")

        return response.json()
