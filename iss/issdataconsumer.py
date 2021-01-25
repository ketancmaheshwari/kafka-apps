#!/usr/bin/env python3

from ast import literal_eval as make_tuple

from kafka import KafkaConsumer

kafka_server = 'localhost:9092'

consumer = KafkaConsumer('issloc', bootstrap_servers = kafka_server)

for msg in consumer:
    longitude, latitude, time = make_tuple(msg.value.decode())
    print(longitude, latitude, time)
