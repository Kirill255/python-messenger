import requests

r = requests.get("http://localhost:5000/status")
print(r.json())

# логинимся
username = "Ivan"
password = "111"
data = {
    "username": username,
    "password": password
}
r = requests.post("http://localhost:5000/login", json=data)
print(r.json())

# отправляем сообщение
while True:
    text = input()  # читаем ввод пользователя из консоли
    data = {
        "username": username,
        "text": text,
        "password": password
    }
    r = requests.post("http://localhost:5000/send", json=data)
    print(r.json())
