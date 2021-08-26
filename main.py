import json
from kafka import KafkaProducer

folderName = "~/kafkaCerts/kafka-pizza/"
producer = KafkaProducer(
    bootstrap_servers="<INSTANCE_NAME>-<PROJECT_NAME>.aivencloud.com:<PORT>",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')

)