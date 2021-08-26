# aiven
This application sends events to a Kafka topic (a producer)  which will then be read by a Kafka consumer application that  you've written.   

The consumer application must then store the  consumed data to an Aiven PostgreSQL database.

It uses python as a programing language

Use this commad on CLI to install Kafka

pip install kafka-python
