import json
import urllib
import os

result = os.system('curl  --header "Authorization: <your_token>" \
      --header "Accept: application/json" \
      --header "Content-Type: application/json" -k https://127.0.0.1/events') 


data = json.load(result)
print(len(data))