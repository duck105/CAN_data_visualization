from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=["GET"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET"])
def data():
    # Data Format [ Time, Velocity, SOC]

    df = pd.read_csv("Arduino1_decode.csv")
    n = 40000
    diff = 2500
    datas = [list(a) for a in zip(list(df.iloc[:n:diff, 0]), list(df.iloc[:n:diff, 6]), list(df.iloc[:n:diff, 1]))]
    print(len(datas))

    response = make_response(json.dumps(datas))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
