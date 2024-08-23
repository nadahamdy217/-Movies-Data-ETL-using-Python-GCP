import os
from google.cloud import pubsub_v1

# Set up the environment variable to point to the local Pub/Sub emulator
os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"

# Set the project ID and topic ID
project_id = "test-project"  # Use your emulator project ID or a placeholder
topic_id = "movies-topic"

# Initialize the Publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Publish a test message
test_message = "This is a test message."
data = test_message.encode("utf-8")
future = publisher.publish(topic_path, data)
print(f"Published test message ID: {future.result()}")

print("Test message published.")
