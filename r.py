import requests


token = 'fce2a2514c2abf28aa822b890e80732edbc010bc'
url = "https://nest.staging.scrapehero.com/api/v1/scheduler/"


headers = {'Authorization': f"Token {token}"}
payload = {
        "action": "stop",
        "run_id": 48366
    }
response = requests.post(url, headers=headers, json=payload)

print(response.content)

