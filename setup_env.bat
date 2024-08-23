@echo off
py -m venv venv
call venv\Scripts\activate
pip install numpy pandas google-cloud-pubsub docker
echo Environment setup completed.
