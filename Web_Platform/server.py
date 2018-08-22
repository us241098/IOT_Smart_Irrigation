import os
from flask import Flask, request, redirect, url_for, render_template
import threading


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    statuses = []
    ids = [0,1,2,3]
    with open('recived.txt') as f:
        statuses = f.read().splitlines()

    return render_template("home.html", statuses=statuses, ids=ids)


def flask_app(app):
    app.run(port = 5001, debug=True)


def launch():
    os.system("python reciver.py")


def main(app):
    t1 = threading.Thread(target=launch, args=())
    t1.start()
    flask_app(app)

if __name__ == "__main__":
    main(app)
