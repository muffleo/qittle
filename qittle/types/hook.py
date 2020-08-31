from pydantic import BaseModel
from typing import Dict


class HookDescription(BaseModel):
    hookId: str
    hookType: str
    hookParameters: Dict[str, str]

    txnType: str


class Response(BaseModel):
    response: str
