from kafka import KafkaConsumer
#import logging
import json
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType
from bs4 import BeautifulSoup
import pymongo

def parse_medium_story_text(link):
    response = requests.get(link)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p', {'class': 'pw-post-body-paragraph'})
    top_two_paragraphs = [p.get_text().strip() for p in paragraphs[:2]]
    story_text = '\n\n'.join(top_two_paragraphs)
    return story_text

def run_spark_consumer_app(topic, KAFKA_BROKER):
    # Create a SparkSession
    spark = SparkSession.builder.appName("KafkaMediumRSSConsumer")\
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1")\
        .getOrCreate()

    schema = StructType([
        StructField("title", StringType(), True),
        StructField("link", StringType(), True),
        StructField("description", StringType(), True),
        StructField("published", StringType(), True),
        StructField("tag", StringType(), True),
    ])

    kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BROKER) \
        .option("subscribe", topic) \
        .load()

    json_df = kafka_df.selectExpr("CAST(value AS STRING) as json") \
        .select(from_json("json", schema).alias("data")) \
        .select("data.*")
    
    # Print the schema of the json DataFrame for debugging
    json_df.printSchema()

    # Write the stream to console for testing
    query = json_df.writeStream \
        .format("console") \
        .outputMode("append") \
        .start()

    query.awaitTermination()

def main():
    KAFKA_BROKER = 'localhost:9092'
    topic = 'rss_feed_topic'

    # Using KafkaConsumer to consume messages directly
    print('Starting Kafka consumer...')
    print('test 12112')
    print('test to add something to consumer of branch testbranch 19 and main branch is ahead')
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda m: json.loads(m.decode('ascii')),
        auto_offset_reset='earliest',
        max_poll_interval_ms=1000
    )
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['test_db']
    collection = db['collection']

    count = 0
    # Consume messages and print their values
    for message in consumer:
        print("Message value:", message.value)
        insert_result = collection.insert_one(json.loads(message.value))
        count += 1
        print('Total number of messages:', count)

if __name__ == '__main__':
    # logging.basicConfig(level="DEBUG")
    try:
        main()
    except KeyboardInterrupt:
        pass
