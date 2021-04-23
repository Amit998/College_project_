# from googlesearch import search

# # print(search("Narendra Modi"))
# results=search("Narendra Modi Times Now")

# for result in results:
#     print(result)


# import requests

# url = "http://www.kite.com"
# timeout = 5
# try:
# 	request = requests.get(url, timeout=timeout)
# 	print("Connected to the Internet")
# except (requests.ConnectionError, requests.Timeout) as exception:
# 	print("No internet connection.")

import math

def log(x, base):
	log_b = 2
	while x != int(round(base ** log_b)):
		# print(round(base ** log_b))
		log_b += 0.01
	# print(log_b)
	return int(round(log_b))


mainVal=1000
base_val=2
print(math.log(mainVal,base_val))
# print(log(mainVal,base_val))