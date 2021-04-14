# from googlesearch import search

# # print(search("Narendra Modi"))
# results=search("Narendra Modi Times Now")

# for result in results:
#     print(result)


import requests

url = "http://www.kite.com"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print("Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection.")