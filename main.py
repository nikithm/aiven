import json
from kafka import KafkaProducer

v = "data"

folderName = "keys/"
producer = KafkaProducer(
    bootstrap_servers="kafka-31ed45d2-nikithbhee-1d6c.aivencloud.com:24572",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')

)