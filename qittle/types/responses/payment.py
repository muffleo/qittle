import base64
import hashlib
import hmac
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SumModel(BaseModel):
    amount: float
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
    commission: Optional[SumModel]

    txnId: str
    personId: int

    comment: Optional[str] = None
    errorCode: Optional[str] = None


class HookModel(BaseModel):
    hookId: str
    messageId: Optional[str] = None
    payment: Optional[PaymentModel] = None
    test: bool
    version: str
    hash: Optional[str] = None

    def verify(self, key: str) -> bool:
        sign_fields = "{currency}|{sum}|{type}|{account}|{txn_id}".format(
            type=self.payment.type, account=self.payment.account,
            sum=self.payment.sum, currency=self.payment.sum.currency,
            txn_id=self.payment.txnId,
        )

        webhook_key = base64.b64decode(bytes(key, 'utf-8'))
        payment_hash = hmac.new(
            key=webhook_key, msg=sign_fields.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

        return self.hash == payment_hash
