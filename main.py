import requests

URL = "https://techy-api.vercel.app/api/json"

response = requests.get(URL)
print(response.json())