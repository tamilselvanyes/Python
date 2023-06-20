import json

import requests

URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=URL)

response.raise_for_status()

data = response.json()

print(data["iss_position"])

# if response.status_code == 404:
#     raise Exception("The requested source does not exist")
# elif response.status_code == 300:
#     raise Exception("You are not authenticated")
# else:
#     print("Successful")
