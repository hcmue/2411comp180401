import json
import requests

res = requests.get("https://www.hcmue.io.vn")
# print(res)

if res.status_code == 200:
    print(res.content)

r2 = requests.get("https://jsonplaceholder.typicode.com/comments")
if r2.status_code == 200:
    print(json.dumps(r2.json(), indent=3))