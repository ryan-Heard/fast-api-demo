from kafka.admin import KafkaAdminClient, NewTopic
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_kafka_topic(client_id, topic_name, partitions=1, replication_factor=1) -> bool:
    # Check if topic already exists
    # If not create topic

    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092",
        client_id=client_id
    )

    topic_list = []
    existing_topics = admin_client.list_topics()
    if topic_name in existing_topics:
        logger.info(f"Topic '{topic_name}' already exists")
        return False
    topic_list.append(
        NewTopic(name=topic_name, num_partitions=partitions, replication_factor=replication_factor))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    logger.info(f"Topic '{topic_name}' created")

    return True


if __name__ == "__main__":
    create_kafka_topic("test_client", "test_topic", 3, 1)
