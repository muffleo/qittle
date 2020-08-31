from typing import List, AsyncIterable
from asyncio import iscoroutinefunction

from qittle.types.payment import Payment


class HandlingProvider:
    def __init__(self):
        self.__handlers: List[dict] = []

    def __call__(self, **kwargs):
        def decorator(func):
            if not iscoroutinefunction(func):
                raise Exception("handler function should be 'async'")

            self.__handlers.append(
                {"function": func, "payload": kwargs}
            )
            return func

        return decorator

    @property
    async def __share_on_air(self) -> AsyncIterable[dict]:
        for handler in self.__handlers:
            yield handler

    async def check(self, payment: Payment):
        if payment is None:
            return

        async for handler in self.__share_on_air:
            if handler["payload"] is None or (
                {**payment.dict(), **handler["payload"]} == payment.dict()
            ):
                await handler["function"](payment)
