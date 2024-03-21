import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + "helloworld/1",{"likes":10,"name":"vid_1","views":1000})
# print(response.json())
# input()
response = requests.get(BASE + "helloworld/1")
print(response.json())