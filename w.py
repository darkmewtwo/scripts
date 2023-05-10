import requests
import json

token = 'fce2a2514c2abf28aa822b890e80732edbc010bc'
url = "https://nest.staging.scrapehero.com/api/v1/scheduler/"
headers = {'Authorization': f"Token {token}"}
payload = {
        "action": "start",
        "spider_id": 504,
        "production": True,
        "branch": 'master'
    }
    
print(headers)
response = requests.post(url, headers=headers, json=payload)

print(response.content)
j = response.content.decode('utf-8')
print(j, type(j))
print(bytes(j, 'utf-8'))
print(json.loads(j))
print(response.json(), 'sdsdd')

run_id = json.loads(response.content.decode('utf-8')).get('run_id')
print(run_id)
