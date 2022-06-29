import requests

TECHY_API_URL = "https://techy-api.vercel.app/api/json"

techy_response = requests.get(TECHY_API_URL).json()

print(techy_response['message'])
