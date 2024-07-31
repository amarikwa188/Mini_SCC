from flask import Flask


app: Flask = Flask(__name__)


@app.route("/")
def index() -> str:
    return ""


if __name__ == "__main__":
    pass