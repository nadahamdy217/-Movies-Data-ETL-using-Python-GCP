import os
from google.cloud import pubsub_v1

# Set up the environment variable to point to the local Pub/Sub emulator
os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"

# Set the project ID and other parameters
project_id = "test-project"
topic_id = "movies-topic"
subscription_id = "movies-subscription"

# Set up Pub/Sub client
publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

# Create a topic
project_path = f"projects/{project_id}"
topic_path = publisher.topic_path(project_id, topic_id)
publisher.create_topic(name=topic_path)
print(f"Topic '{topic_id}' created.")

# Create a subscription
subscription_path = subscriber.subscription_path(project_id, subscription_id)
subscriber.create_subscription(name=subscription_path, topic=topic_path)
print(f"Subscription '{subscription_id}' created.")
