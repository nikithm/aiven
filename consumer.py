from kafka import KafkaConsumer
import psycopg2

conn = psycopg2.connect('postgres://avnadmin:d4x37goj4y8m71a1@pg-13e4cc60-nikithbhee-1d6c.aivencloud.com:24570/defaultdb?sslmode=require')

cur = conn.cursor()

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
    cur.execute('''
	CREATE TABLE test (
	key VARCHAR(24) NOT NULL,
	value VARCHAR(24) NOT NULL
	);''')

	
    print("Added:{} = {} to the Postgres DB".format(msg.key,msg.value))