# Installation

## Install Docker
``` shell
sudo yum install docker
```

## Install Docker-compose
Run this command to download the current stable release of Docker Compose:
``` shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Apply executable permissions to the binary:
``` shell
sudo chmod +x /usr/local/bin/docker-compose
```

You can also create a symbolic link to /usr/bin:
``` shell
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## Run

Start docker
``` shell
systemctl start docker
```

``` shell
cd twitter_api
```

Run docker-compose: 
``` shell
docker-compose up -d 
```

## Kafka

Interact with kafka container:
``` shell
docker exec -it kafka /bin/sh 
```

Create a topic:
``` shell
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic tweets
```

List all topics:
``` shell
kafka-topics.sh --list --zookeeper zookeeper:21
```

Produce data:
``` shell
kafka-console-producer.sh --broker-list localhost:9092 --topic tweets
```

Consume data:
``` shell
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic tweets --from-beginning
```

## Check mongodb data

Interact with mongo container:
``` shell
docker exec -it mongo bash 
```

run mongo shell:
``` shell
mongo
```

Use or create tweets db:
``` shell
use tweets;
```

Create tweets collection:
``` shell
db.createCollection("tweets", { capped : true, size : 5242880, max : 5000 } );
```

Check results (after inserting data)
``` shell
db.tweets.find();
```

## Generate data

Run producer to get data from twitter api and send it to kafka topic:
``` shell
python3 producer_request.py 
```

## Consume and store data to mongo
Run this to consume data from a topic and send it to mongo:
``` shell
python3 consumer.py
```
