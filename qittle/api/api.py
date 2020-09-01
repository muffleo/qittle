import typing

from qittle.api.abc import ABCAPI
from qittle.http import (
    ABCSessionManager,
    SessionManager,
    AiohttpClient
)
from qittle.types.categories import APICategories


class API(ABCAPI, APICategories):
    API_URL = "https://edge.qiwi.com/"

    def __init__(
            self,
            token: str,
            session_manager: typing.Optional[SessionManager] = None,
    ) -> None:
        self.token = token
        self.http: ABCSessionManager = session_manager or SessionManager(AiohttpClient)

    async def request(
            self,
            request_method: str,
            api_method: str,
            data: dict,
    ) -> dict:
        async with self.http as session:
            response = await session.request_json(
                request_method,
                url=self.API_URL + api_method,
                data=data, headers={
                    "Authorization": f"Bearer {self.token}"
                }
            )

            return response

    @property
    def instance(self) -> "API":
        return self
