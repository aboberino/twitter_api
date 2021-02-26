import requests
import json
from pprint import pprint
import twitter_credentials
from kafka import KafkaProducer


headers = { 'Authorization': f'Bearer {twitter_credentials.BEARER_TOKEN}'}
res = requests.get('https://api.twitter.com/2/tweets/sample/stream', headers=headers, stream=True)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'])


for response in res.iter_lines():
    pprint(json.loads(response))
    producer.send("tweets", response)
