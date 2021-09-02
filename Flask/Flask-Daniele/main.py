import requests
import json

ENDPOINT_1 = 'http://localhost:8080/say/hi'
ENDPOINT_2 = 'http://localhost:8080/say/hello'

name = 'Marco'

response_1 = requests.post(ENDPOINT_1, json='')
response_2 = requests.post(ENDPOINT_2, json=name)

output_1 = json.loads(response_1.content)
output_2 = json.loads(response_2.content)

print(output_1)
print(output_2)