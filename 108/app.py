from flask import Flask, send_from_directory, make_response
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "Alpaca{**********************************************REDACTED**********************************************}")


@app.route("/")
def index():
    resp = make_response(send_from_directory(".", "index.html"))
    resp.set_cookie("flag", FLAG)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10800, debug=False)
