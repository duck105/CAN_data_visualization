from flask import Flask, render_template, jsonify, abort, request
import random
import json
import time
from random import random

app = Flask(__name__)

data_points = [
    {   
        'id': 0,
        'time': time.time()*1000,
        'velocity': 100,
        'soc': 50
    }
]

# 首頁(realtime 資料)
@app.route('/', methods=["GET"])
def main():
    return render_template('index.html')

# 歷史資料，未完成
@app.route('/analysis', methods=["GET"])
def render_analysis():
    return render_template('analysis.html')

# 接收Rpi上傳的資料
@app.route('/points', methods=["POST"])
def create_data():
    if not request.json or not 'time' in request.json:
        abort(400)
    
    point = {
        'id': request.json['id'],
        'time': request.json['time'],
        'velocity': request.json['velocity'],
        'soc': request.json['soc']
    }
    data_points.append(point)
    return jsonify(point), 201

# 前端(index.html) 獲取資料，每次都只拿最新一筆加入圖表中
@app.route('/data', methods=["GET"])
def get_data():
    # Data Format {'time': t, 'velocity': v, 'soc': soc}
    return jsonify(data_points[-1])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
