from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "demo-topic",
    bootstrap_servers="getting-started-with-kafka.htn-aiven-demo.aivencloud.com:17705",
    client_id="demo-client-1",
    group_id="demo-group",
    security_protocol="SSL",
    ssl_cafile="ca.crt",
    ssl_certfile="client.crt",
    ssl_keyfile="client.key",
)

for msg in consumer:
    print("Received: {}".format(msg.value))