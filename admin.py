from kafka import KafkaAdminClient
from kafka.admin import NewTopic # type: ignore

def create_kafka_topic(topic_name, num_partitions=2, replication_factor=1):
    # Create an Admin client
    admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')

    # Create a new topic
    new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)

    # Create the topic
    try:
        admin_client.create_topics([new_topic])
        print(f"Topic '{topic_name}' created successfully.")
    except Exception as e:
        print(f"Failed to create topic '{topic_name}': {e}")
    finally:
        admin_client.close()

# Usage example
if __name__ == "__main__":
    topic_name = "rss_feed_topic"  # Replace with your desired topic name
    create_kafka_topic(topic_name)
