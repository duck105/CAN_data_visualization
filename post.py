# 跑在Rpi 上負責送資料過去server的code 
import requests
import time
from random import random

def post_data(id):
    URL = "http://localhost:5000/points"

    # data to be sent to server 
    data = {'id': id,
            'time': time.time()*1000, 
            'velocity': id,
            'soc': random() * 100} 
    
    # sending post request and saving response as response object 
    r = requests.post(url = URL, json = data) 
    
    # extracting response text  
    response = r.text 
    print("The response is:%s" % response) 

def run():
    id = 0
    while True:
        post_data(id)
        time.sleep(0.25)
        id += 1

if __name__ == "__main__":
    run()