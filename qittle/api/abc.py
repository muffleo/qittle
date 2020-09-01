from abc import ABC, abstractmethod

from qittle.http import ABCSessionManager


class ABCAPI(ABC):

    http: ABCSessionManager

    @abstractmethod
    async def request(
            self,
            request_method: str,
            api_method: str,
            data: dict,
    ) -> dict:
        pass
