import json
from kafka import KafkaProducer


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

producer.send("test-topic",
                key={"key": 2},
                value={"message": "hello world 2"}
            )
producer.flush()