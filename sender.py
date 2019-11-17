import requests

r = requests.get("http://localhost:5000/status")
print(r.json())

# логинимся
username = "Ivan"
password = "111"
login_data = {
    "username": username,
    "password": password
}
r = requests.post("http://localhost:5000/login", json=login_data)
print(r.json())

# отправляем сообщение
while True:
    text = input()  # читаем ввод пользователя из консоли
    data = {
        "username": username,
        "text": text,
        "password": password
    }
    # логинимся перед каждым запросом, т.к. пользователи у нас хранятся по сути в памяти, и после перезагрузки сервера, наш users сбрасывается в начальное состояние, это решается с помощью бд
    requests.post("http://localhost:5000/login", json=login_data)
    r = requests.post("http://localhost:5000/send", json=data)
    print(r.json())
