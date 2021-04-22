API_KEY="AIzaSyA1pyVD1l9uHnFks-6ZAHlEy-6xANuEWeM"

import requests
from urllib.parse import urlencode
import json

# data_type="json"
# endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# params = {"address": "Sanhati Pally, Katwa, West Bengal 713130", "key": API_KEY}
# url_params=urlencode(params)
# print(url_params)
# url=f"{endpoint}?{url_params}"
# print(url)


def extract_lat_lang(address_or_postal_code,data_type='json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postal_code, "key": API_KEY}
    url_params=urlencode(params)
    # print(url_params)
    url=f"{endpoint}?{url_params}"
    r=requests.get(url)
    print(r.json())
    if (r.status_code not in range(200,299)):
        return {}
    return r.json()['results'][0].keys()

print(extract_lat_lang("Sanhati Pally, Katwa, West Bengal 713130"))