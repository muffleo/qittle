from json import JSONDecodeError
from typing import Union

from pydantic import ValidationError
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from starlette.routing import Route
from uvicorn import run

from qittle.hook.handler import HandlingProvider
from qittle.types.responses.payment import HookModel


class Server:
    def __init__(
            self,
            key: str,
            provider: HandlingProvider,
    ) -> None:
        self.key = key
        self.provider = provider
        self.app = Starlette(
            routes=[
                Route("/", self.acceptor, methods=["POST"])
            ]
        )

    def run(self) -> None:
        run(self.app, host="0.0.0.0", port=80)

    async def acceptor(self, request: Request) -> Union[Response, PlainTextResponse]:
        try:
            hook = HookModel(**await request.json())
        except (JSONDecodeError, ValidationError):
            return Response(status_code=500)

        if not hook.verify(self.key):
            return Response(status_code=401)

        await self.provider.check(hook.payment)
        return PlainTextResponse("OK", status_code=200)
