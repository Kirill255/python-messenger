from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {
        "status": True,
        # "time": datetime.now()
        # "time": str(datetime.now())
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


if __name__ == "__main__":
    app.run()
