import os

from qittle import Listener, PaymentModel
from qittle.utils.logger import logger

listener = Listener(
    os.getenv("QIWI_TOKEN"), address="address"
)  # Instantiate listener with given address and token


@listener.event(account="+79991234567")
async def handler_with_rules(_: PaymentModel) -> None:
    """
    This handler catches hooks
    that match the given parameters.
    """
    logger.success("Captured payment!")


listener.listen()  # Run server
