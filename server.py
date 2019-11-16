from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)
messages = [
    {"username": "Jack", "time": time.time(), "text": "Hello"},
    {"username": "Jane", "time": time.time(), "text": "Hi, Jack"},
]


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
    input: {"username": str, "text": str}
    :return: {"status": bool}
    """
    print(request.json)
    username = request.json["username"]
    text = request.json["text"]

    # messages.insert(0, {"username": username, "time": time.time(), "text": text})
    messages.append({"username": username, "time": time.time(), "text": text})

    return {"status": True}


if __name__ == "__main__":
    app.run()
