from flask import Flask, render_template, request
from http.client import HTTPConnection
from urllib.parse import urlparse, ParseResult


app: Flask = Flask(__name__)


def check_site(url, timeout=5) -> bool:
    parser: ParseResult = urlparse(url)
    host_name: str = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection: HTTPConnection = HTTPConnection(host=host_name, port=port,
                                                    timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as ex:
            print(ex, ex.with_traceback)
        finally:
            connection.close()


@app.route("/", methods=["post", "get"])
def index() -> str:
    is_online = False
    notify: bool = False

    if request.method == "POST":
        url: str = request.form["url"]
        is_online: bool = check_site(url)
        notify = True

        return render_template("index.html", url=url, status=is_online,
                            notify=notify)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)