from flask import Flask, render_template, request


app: Flask = Flask(__name__)


@app.route("/", methods=["post", "get"])
def index() -> str:
    if request.method == "POST":
        url: str = request.form["url"]
        print(f"\n{url}\n")

    is_online: bool = True 
    return render_template("index.html", status=is_online)


if __name__ == "__main__":
    app.run(debug=True)