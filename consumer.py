from kafka import KafkaConsumer
#import logging
import json

def main() :
    consumer = KafkaConsumer(
        'rss_feed_topic',
        bootstrap_servers = ['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('ascii')),
        auto_offset_reset='earliest',
        max_poll_interval_ms = 1000
    )
    count=0
    for message in consumer:
        print(message.value)
        count+=1
        print('Total no of messages : ',count)
    
    
    

if __name__ == '__main__' :
    #logging.basicConfig(level= "DEBUG")
    try :
        main()
    except KeyboardInterrupt :
        pass