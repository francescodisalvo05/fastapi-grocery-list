import requests

BASE = 'http://127.0.0.1:5000/'

data = [
    {"name" : "AA", "likes" : 10, "views" : 2},
    {"name" : "BB", "likes" : 15, "views" : 33},
    {"name" : "CC", "likes" : 1, "views" : 5}
]

# response = requests.put(BASE + "video/1", {"name" : "Name1", "likes" : 10, "views" : 5})
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.delete(BASE + "video/0")
print(response)