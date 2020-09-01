import os

from qittle import Listener, PaymentModel
from qittle.utils.logger import logger

listener = Listener(
    os.getenv("QIWI_TOKEN"), address="address"
)  # Instantiate listener with given address and token


@listener.event()
async def simple_handler(_: PaymentModel):
    """This handler catches all hooks"""
    logger.success("Captured payment!")


listener.listen()  # Run server
