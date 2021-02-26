from kafka import KafkaConsumer
from pymongo import MongoClient

from json import loads
import json

consumer = KafkaConsumer("tweets",
bootstrap_servers=['localhost:9092'],
auto_offset_reset='earliest',
#enable_auto_commit=True,
group_id='my-group',
consumer_timeout_ms=1000,
value_deserializer=lambda x: loads(x.decode('utf-8')))


client = MongoClient('localhost', 27017)
db = client.tweets
tweets = db.tweets

if __name__ == "__main__":
    for message in consumer:
        msg = message.value
        consumer.commit()
        #msg_json = json.loads(msg)
        print(tweets.insert_one(msg['data']).inserted_id)
