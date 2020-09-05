from qittle.types.responses import hook
from .base import Base


class HookCategory(Base):
    async def register(
            self,
            param: str,
            hookType: int = 1,
            txnType: str = 2,
            **kwargs
    ) -> hook.DescriptionModel:
        params = self.get_set_params(locals())
        return hook.DescriptionModel(
            **await self.api.request(
                "PUT", "payment-notifier/v1/hooks",
                params
            )
        )

    async def get(
            self,
            **kwargs,
    ) -> hook.DescriptionModel:
        params = self.get_set_params(locals())
        return hook.DescriptionModel(
            **await self.api.request(
                "GET", "payment-notifier/v1/hooks/active",
                params
            )
        )

    async def delete(
            self,
            hookId: str,
            **kwargs,
    ) -> hook.ResponseModel:
        params = self.get_set_params(locals())
        return hook.ResponseModel(
            **await self.api.request(
                "DELETE", f"payment-notifier/v1/hooks/{hookId}",
                params
            )
        )

    async def trigger(
            self,
            **kwargs,
    ) -> hook.ResponseModel:
        params = self.get_set_params(locals())
        return hook.ResponseModel(
            **await self.api.request(
                "GET", "payment-notifier/v1/hooks/test",
                params
            )
        )
