import json
from datetime import datetime

import requests

URL = "http://api.open-notify.org/iss-now.json"

SUN_RISE_SET = "https://api.sunrise-sunset.org/json"

LAT = 13.0615
LNG = 80.2207

response = requests.get(url=URL)

response.raise_for_status()

data = response.json()

# print(data["iss_position"])

# if response.status_code == 404:
#     raise Exception("The requested source does not exist")
# elif response.status_code == 300:
#     raise Exception("You are not authenticated")
# else:
#     print("Successful")

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

sun_info = requests.get(url = SUN_RISE_SET, params= parameters)

sun_info_json = sun_info.json()

sunrise_hour = sun_info_json["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = sun_info_json["results"]["sunset"].split("T")[1].split(":")[0]

print(sunset_hour,sunrise_hour)

time_now = datetime.now()

print(time_now)


