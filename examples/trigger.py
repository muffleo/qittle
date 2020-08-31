from qittle.api import API
from qittle.api import hook

api = API("token")  # Instantiate API class
print(hook.trigger_hook(api).response)  # Call API method and print response
