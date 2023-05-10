import requests
from concurrent.futures import ThreadPoolExecutor
import threading

url = "https://nest.staging.scrapehero.com/api/v1/rules/run_qa/"

# url = "https://nest.scrapehero.com/api/v1/scheduler/"

ch = {'Authorization': 'Token 741ab1c7b342580b3f5b7baf19837a78539d475c'}
# pdn
# ch = {'Authorization': 'Token b837cbb1fe1618ed693b2f72c646fe90ebd2531c'}


pay = {"dataset_id":"81348"}

r = requests.post(url, json=pay, headers=ch)
print(r)
