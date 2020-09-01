import asyncio
import os

from qittle.api import API

api = API(os.getenv("QIWI_TOKEN"))


async def main():
    response = await api.hook.trigger()  # Call API method..
    print(response.response)  # ..and print response

asyncio.run(main())
