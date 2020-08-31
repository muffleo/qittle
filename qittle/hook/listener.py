from qittle import api
from qittle.utils.exceptions import QiwiError

from qittle.hook.server import Server
from qittle.hook.handler import HandlingProvider

from typing import Optional
from pyngrok import ngrok


class Listener:
    def __init__(self, token: str, address: Optional[str] = None) -> None:
        self.__address = address or ngrok.connect()
        self.__b64_encoded_key: Optional[str] = None

        self.event = HandlingProvider()
        self.api = api.API(token)

    def setup(self) -> None:
        try:
            hook = api.hook.get_hook(self.api)
        except QiwiError:
            api.hook.delete_hook(self.api, hid=hook.hookId)
            hook = api.hook.register_hook(self.api, server=self.__address)

        self.__b64_encoded_key = api.key.change_key(self.api, hook.hookId)

    def run(self) -> None:
        if not self.__b64_encoded_key:
            raise Exception("Base64-encoded key not found")

        Server(self.__b64_encoded_key, self.event).run()
