from asyncio import AbstractEventLoop, get_event_loop
from typing import Optional

from pyngrok import ngrok

from qittle.api import API
from qittle.hook.handler import HandlingProvider
from qittle.hook.server import Server
from qittle.utils.exceptions import QiwiError


class Listener:
    def __init__(
            self,
            token: str,
            address: Optional[str] = None,
            loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        self.__loop = loop or get_event_loop()
        self.__address = address or ngrok.connect()
        self.__b64_encoded_key: Optional[str] = None

        self.event = HandlingProvider()
        self.api = API(token)

    def listen(self) -> None:
        self.__loop.run_until_complete(self.setup())

        if not self.__b64_encoded_key:
            raise Exception("Base64-encoded key not found")

        Server(self.__b64_encoded_key, self.event).run()

    async def setup(self) -> None:
        try:
            hook = await self.api.hook.get()
        except QiwiError:
            await self.api.hook.delete(hook.hookId)
            hook = await self.api.hook.register(self.__address)

        self.__b64_encoded_key = await self.api.key.change(hook.hookId)
