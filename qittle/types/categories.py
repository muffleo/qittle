import typing
from abc import ABC, abstractmethod

from qittle.types.methods import *

if typing.TYPE_CHECKING:
    from qittle.api import API


class APICategories(ABC):
    @property
    def hook(self) -> hook.HookCategory:
        return hook.HookCategory(self.instance)

    @property
    def key(self) -> key.KeyCategory:
        return key.KeyCategory(self.instance)

    @property
    @abstractmethod
    def instance(self) -> "API":
        pass
