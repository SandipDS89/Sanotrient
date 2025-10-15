import requests
import json

url = "http://127.0.0.1:5000/recommend"
payload = {
    "age": 21,
    "gender": "male",
    "weight": 47,
    "height": 165,
    "activity": "moderate",
    "goal": "weight_gain",
    "preference": "non-veg",
    "allergen": "none"
}

r = requests.post(url, json=payload)
print(json.dumps(r.json(), indent=2))
