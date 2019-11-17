from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)
messages = [
    {"username": "Jack", "time": time.time(), "text": "Hello"},
    {"username": "Jane", "time": time.time(), "text": "Hi, Jack"},
]
# что-то вроде хранилища паролей, где ключ это username, а значение какой-то пароль
users = {
    "Jack": "123",
    "Jane": "321"
}


@app.route("/")
def hello_view():
    return "Hello, World! This is a messenger!"


@app.route("/status")
def status_view():
    return {
        "status": True,
        # "time": datetime.now()
        # "time": str(datetime.now())
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.route("/messages")
def messages_view():
    return {"messages": messages}


@app.route("/send", methods=["POST"])
def send_view():
    """
    Отправить сообщение всем
    input: {"username": str, "text": str, "password": str}
    :return: {"status": bool}
    """
    print(request.json)
    username = request.json["username"]
    text = request.json["text"]
    password = request.json["password"]

    # если нет пользователя или неверный пароль
    if username not in users or users[username] != password:
        return {"status": False}

    # messages.insert(0, {"username": username, "time": time.time(), "text": text})
    messages.append({"username": username, "time": time.time(), "text": text})

    return {"status": True}


@app.route("/login", methods=["POST"])
def login_view():
    """
    Логиним пользователя в системе
    input: {"username": str, "password": str}
    :return: {"status": bool}
    """
    print(request.json)
    username = request.json["username"]
    password = request.json["password"]

    # если нет пользователя
    if username not in users:
        users[username] = password  # то записываем нового пользователя
        return {"status": True}
    elif users[username] == password:  # если есть пользователь, то сверяем пароль
        return {"status": True}
    else:
        return {"status": False}


if __name__ == "__main__":
    app.run()
