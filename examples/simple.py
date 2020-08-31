from qittle import Listener, Payment
from qittle.utils.logger import logger

listener = Listener(
    "domain", "token"
)  # Instantiate listener with given address and token


@listener.event()
async def _(payment: Payment):
    logger.success("Captured payment!")


listener.setup()  # Setup hook
listener.run("0.0.0.0", 80)  # Run server
