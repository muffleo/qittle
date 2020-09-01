from qittle.types.responses import hook
from .base import Base


class HookCategory(Base):
    async def register(
            self,
            server: str,
            **kwargs,
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
            hook_id: str,
            **kwargs,
    ) -> hook.ResponseModel:
        params = self.get_set_params(locals())
        return hook.ResponseModel(
            **await self.api.request(
                "DELETE", "payment-notifier/v1/hooks/active",
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
