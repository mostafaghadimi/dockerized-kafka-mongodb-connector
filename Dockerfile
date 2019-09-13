FROM wurstmeister/kafka

RUN apk add -y python3
RUN pip3 install kafka-python
RUN pip3 install pymongo

COPY ./files/consumer.py /opt/kafka
COPY ./files/producer.py /opt/kafka