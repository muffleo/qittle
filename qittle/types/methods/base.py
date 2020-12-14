import typing

from qittle.utils.dev import to_camel_case

if typing.TYPE_CHECKING:
    from qittle.api import API


class Base:
    def __init__(self, api: "API") -> None:
        self.api = api

    @classmethod
    def get_set_params(cls, params: dict) -> dict:
        exclude_params = params.copy()
        exclude_params.update(params["kwargs"])
        exclude_params.pop("kwargs")
        return {
            to_camel_case(k) if not k.endswith("_") and "_" in k else (k[:-1] if k.endswith("_") else k): v
            for k, v in exclude_params.items()
            if k != "self" and v is not None
        }

    @classmethod
    def construct_api(cls, api: "API") -> typing.Type["Base"]:
        cls.api = api
        return cls