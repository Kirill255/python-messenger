from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {"status": "ok", "time": datetime.now()}


if __name__ == "__main__":
    app.run()
