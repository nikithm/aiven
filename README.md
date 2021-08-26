## aiven
This application sends events to a Kafka topic (a producer)  which will then be read by a Kafka consumer application that  you've written.   

The consumer application must then store the  consumed data to an Aiven PostgreSQL database.

It uses python as a programing language

Use this commad on CLI to install Kafka:
pip install kafka-python

First run #consumer.py 
to listen

Then run #producer.py 
to send messages and upfate it to PostgreSQL database.


For Consumer you also need to install psycopg2

Use this commad on CLI to install psycopg2:
pip install psycopg2
