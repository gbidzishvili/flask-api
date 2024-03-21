import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes":78,"name":"name_1","views":45646226},
    {"likes":10,"name":"name_2","views":13424234234},
    {"likes":345,"name":"name_3","views":1034500}
]
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i),data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/1")
print(response.json())



