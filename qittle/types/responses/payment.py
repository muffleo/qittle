import base64
import hashlib
import hmac
import typing

from datetime import datetime
from pydantic import BaseModel


class SumModel(BaseModel):
    amount: typing.Union[int, float]
    currency: int


class PaymentModel(BaseModel):
    type: str
    status: str
    account: str
    provider: int
    date: datetime
    signFields: str
    sum: SumModel
    total: SumModel
    commission: typing.Optional[SumModel]

    txnId: str
    personId: int

    comment: typing.Optional[str] = None
    errorCode: typing.Optional[str] = None


class HookModel(BaseModel):
    hookId: str
    messageId: typing.Optional[str] = None
    payment: typing.Optional[PaymentModel] = None
    test: bool
    version: str
    hash: typing.Optional[str] = None

    def verify(self, key) -> bool:
        sign_fields = "{currency}|{sum}|{type}|{account}|{txn_id}".format(
            type=self.payment.type, account=self.payment.account,
            sum=self.payment.sum.amount, currency=self.payment.sum.currency,
            txn_id=self.payment.txnId,
        )

        webhook_key = base64.b64decode(bytes(key.key, 'utf-8'))
        payment_hash = hmac.new(
            key=webhook_key, msg=sign_fields.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()
        return self.hash == payment_hash
