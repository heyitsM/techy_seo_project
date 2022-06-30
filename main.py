import requests
import pandas as pd

TECHY_API_URL = "https://techy-api.vercel.app/api/json"

responses = {}

for i in range(20):
    techy_response = requests.get(TECHY_API_URL).json()['message']
    responses['i'] = techy_response

data = pd.DataFrame.from_dict(responses, orient="index", columns=["num", "data"])
print(data)


#lets create a chat bot that 