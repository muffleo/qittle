from qittle.types.responses import key
from .base import Base


class KeyCategory(Base):
    async def get(
            self,
            hook_id: str,
            **kwargs,
    ) -> key.KeyModel:
        params = self.get_set_params(locals())
        return key.KeyModel(
            **await self.api.request(
                "GET", f"payment-notifier/v1/hooks/{hook_id}/key",
                params
            )
        )

    async def change(
            self,
            hook_id: str,
            **kwargs,
    ) -> key.KeyModel:
        params = self.get_set_params(locals())
        return key.KeyModel(
            **await self.api.request(
                "POST", f"payment-notifier/v1/hooks/{hook_id}/newkey",
                params
            )
        )
