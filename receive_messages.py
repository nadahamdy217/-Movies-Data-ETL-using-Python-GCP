import os
from google.cloud import pubsub_v1

# Set up the environment variable to point to the local Pub/Sub emulator
os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"

# Set the project ID and other parameters
project_id = "test-project"
subscription_id = "movies-subscription"
subscription_path = f"projects/{project_id}/subscriptions/{subscription_id}"

# Set up Pub/Sub client
subscriber = pubsub_v1.SubscriberClient()

def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()

# Subscribe to the topic
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}...")

# Keep the main thread alive
try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
