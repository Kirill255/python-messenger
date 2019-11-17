import requests

r = requests.get("http://localhost:5000/status")
print(r.json())

r = requests.get("http://localhost:5000/messages")
print(r.json())

r = requests.post("http://localhost:5000/send", json={"username": "Mary", "text": "I love you"})
print(r.json())
