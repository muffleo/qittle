import typing, json

from qittle.api.abc import ABCAPI
from qittle.http import (
    ABCSessionManager,
    SessionManager,
    AiohttpClient
)
from qittle.types.categories import APICategories
from qittle.utils.exceptions import QiwiError


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
            data: typing.Optional[dict] = None,
    ) -> typing.Union[dict, None]:
        async with self.http as session:
            response = await session.request_text(
                request_method,
                url=self.API_URL + api_method,
                data=data or {}, headers={
                    "Authorization": f"Bearer {self.token}"
                }
            )

            try:
                response = json.loads(response)
            except json.JSONDecodeError:
                return

            if "errorCode" in response:
                return

            return response

    @property
    def instance(self) -> "API":
        return self
