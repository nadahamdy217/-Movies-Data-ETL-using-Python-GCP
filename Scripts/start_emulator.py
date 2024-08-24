import os

# Start the Pub/Sub emulator in a Docker container
os.system("docker run -d --name pubsub-emulator -p 8085:8085 google/cloud-sdk gcloud beta emulators pubsub start --host-port=0.0.0.0:8085")
print("Pub/Sub emulator started.")
