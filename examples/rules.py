from qittle import Listener, Payment
from qittle.utils.logger import logger

listener = Listener(
    "token", address="address"
)  # Instantiate listener with given address and token


@listener.event(account="+79991234567")
async def _(payment: Payment) -> None:
    """
    This handler catches hooks
    that match the given parameters.
    """
    logger.success("Captured payment!")


listener.setup()  # Setup hook
listener.run("0.0.0.0")  # Run server
