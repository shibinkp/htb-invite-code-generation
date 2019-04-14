import requests
import base64
import json

url = "https://www.hackthebox.eu/api/invite/generate"
data = requests.post( url )
print base64.b64decode(json.loads(data.text)["data"]["code"])
