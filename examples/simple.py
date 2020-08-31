from qittle import Listener, Payment
from qittle.utils.logger import logger

listener = Listener(
    "token", address="address"
)  # Instantiate listener with given address and token


@listener.event()
async def _(payment: Payment):
    """This handler catches all hooks"""
    logger.success("Captured payment!")


listener.setup()  # Setup hook
listener.run()  # Run server
