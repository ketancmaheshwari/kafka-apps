#!/usr/bin/env python3

import requests, json
import time
import datetime
from kafka import KafkaProducer

url = "http://api.open-notify.org/iss-now.json"
kafka_server = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=kafka_server)

while True:
    response = requests.get(url)
    loc = response.json()
    #msg = datetime.datetime.fromtimestamp( int(loc["timestamp"])).strftime('%Y-%m-%d %H:%M:%S'),loc["iss_position"],loc["message"]
    location = loc["iss_position"]
    latitude = location["latitude"]
    longitude = location["longitude"]
    msg = (longitude, latitude, loc["timestamp"])
    producer.send('issloc', bytes(str(msg), 'utf-8'))
    print(".", end=" ", flush=True)
    time.sleep(5)
