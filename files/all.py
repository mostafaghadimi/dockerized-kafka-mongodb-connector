from kafka import KafkaConsumer, KafkaProducer
from pymongo import MongoClient
from json import loads, dumps
from time import sleep

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    producer.send('mostafa', value=data)
    sleep(5)

consumer = KafkaConsumer(
    'mostafa',
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('mongo:27017')
collection = client.mostafa.mostafa

for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))