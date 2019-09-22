from flask import Flask
from datetime import datetime
import time

app = Flask(__name__)
messages = [
    {"username": "Jack", "time": time.time(), "text": "Hello"},
    {"username": "Jane", "time": time.time(), "text": "Hi, Jack"},
]


@app.route("/")
def hello_view():
    return "Hello, World!"


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


if __name__ == "__main__":
    app.run()
