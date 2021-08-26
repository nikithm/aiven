from kafka import KafkaConsumer

folderName = "keys/"

consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers="kafka-31ed45d2-nikithbhee-1d6c.aivencloud.com:24572",
    client_id="demo-client-1",
    group_id="demo-group",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key"
)

for msg in consumer:
    print("Received:{} = {}".format(msg.key,msg.value))