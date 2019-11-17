import requests

r = requests.get("http://localhost:5000/status")
print(r.json())

r = requests.get("http://localhost:5000/messages")
print(r.json())


data = {
    "username": "Jane",
    "text": "How are you Jack?",
    "password": "321"
}
r = requests.post("http://localhost:5000/send", json=data)
print(r.json())
