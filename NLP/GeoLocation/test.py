from pprint import pprint
import googlemaps
import API_KEY

api_key=API_KEY.API_KEY

map_client=googlemaps.Client(api_key)
# print(dir(map_client))

work_place_address="1 market st, San Francisco , CA"

response=map_client.geocode(work_place_address)
pprint(response)
print(response[0])