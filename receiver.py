from time import sleep

import requests

r = requests.get("http://localhost:5000/status")
print(r.json())

while True:
    r = requests.get("http://localhost:5000/messages")
    # print(r.json())  # с сервера приходит json со свойством messages(список)

    # проходим по этому списку и выводим каждое сообщение
    for message in r.json()["messages"]:
        print(message)
    sleep(1)
