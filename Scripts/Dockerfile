# Use the official Python image from the Docker Hub
FROM python:3.12.5-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required libraries
RUN pip install --no-cache-dir numpy pandas google-cloud-pubsub scipy matplotlib seaborn subprocess

# Command to start the Pub/Sub emulator (if needed)
CMD ["gcloud", "beta", "emulators", "pubsub", "start", "--host-port=0.0.0.0:8085"]
