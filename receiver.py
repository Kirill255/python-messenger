from time import sleep

import requests

r = requests.get("http://localhost:5000/status")
print(r.json())

last_time = 0  # изначально время равно 0, перед запуском цикла, то есть в первый раз мы получим всю историю переписки

while True:
    r = requests.get("http://localhost:5000/messages", params={"after": last_time})  # запрашиваем сообщения
    # print(r.json())  # с сервера приходит json со свойством messages(список)

    # проходим по этому списку и выводим каждое сообщение
    for message in r.json()["messages"]:
        print(message)
        last_time = message["time"]  # метка времени последнего полученного сообщения

    sleep(1)
