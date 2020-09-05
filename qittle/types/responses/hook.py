from typing import Dict

from pydantic import BaseModel


class DescriptionModel(BaseModel):
    hookId: str
    hookType: str
    hookParameters: Dict[str, str]

    txnType: str


class ResponseModel(BaseModel):
    response: str
