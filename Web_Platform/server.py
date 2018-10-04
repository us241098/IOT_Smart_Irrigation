import os
from flask import Flask, request, redirect, url_for, render_template
import threading
import pandas as pd


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    readings = []
    timestamp=[]
    sensor = [0,1,2,3]
    df=pd.read_csv('read.csv')

    for index, row in df.iterrows():
		readings.append(row['sensor'])
		timestamp.append(row['timestamp'])
		print '4342'
    return render_template("home.html", readings=readings,sensor=sensor,timestamp=timestamp)



def flask_app(app):
    app.run(port = 5051, debug=True)


def launch():
    os.system("python reciver.py")


def main(app):
    t1 = threading.Thread(target=launch, args=())
    t1.start()
    flask_app(app)

if __name__ == "__main__":
    main(app)
