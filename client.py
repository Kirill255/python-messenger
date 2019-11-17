import requests

r = requests.get("http://localhost:5000/status")
print(r.json())

r = requests.get("http://localhost:5000/messages")
print(r.json())

# логинимся
data = {
    "username": "Ivan",
    "password": "111"
}
r = requests.post("http://localhost:5000/login", json=data)
print(r.json())

# отправляем сообщение
data = {
    "username": "Ivan",
    "text": "Hello all",
    "password": "111"
}
r = requests.post("http://localhost:5000/send", json=data)
print(r.json())
