import requests
from pathlib import Path

url = "http://mlb.dev.scrapehero.com:10327/get_key"
pub_key_loc = f"{Path.home()}/.ssh/id_rsa.pub"
signed_key_loc = f"{Path.home()}/.ssh/ashley-signed.key"
email = "ashley@scrapehero.com"

with open(pub_key_loc, "r") as file:
    pub_key = file.read().strip("\n")

response = requests.post(
    url,
    data={
        "email": email,
        "pub_key": pub_key
    }
).json()
print(response)
with open(signed_key_loc, "w") as file:
    file.write(response['signed_key'])
