# Unofficial Kafka to MongoDB Sink Connector

As you can see in [this link](https://github.com/mongodb/mongo-kafka/tree/master/docker), which is official mongodb repository, the way they implement a connection between kafka and mongodb is so complicated for a simple purpose. They have used many images that are also not the official version of the images and some of them are not necessary. So, I decided to create a new way to implement the connection. I hope you enjoy. 

## How to run the project?

1. `docker-compose up`

2. `docker exec -it bash`

3. `cd opt/kafka` (change directory to the location where the scripts are located)

4. execute the `bin/kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic mostafa` to create a new topic named 'mostafa'

5. To make sure that above command works properly, try: `bin/kafka-topics.sh --list --bootstrap-server kafka:9092`


6. Run the python code


