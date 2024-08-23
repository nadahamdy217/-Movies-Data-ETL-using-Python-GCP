STEPS:
______

First: you can enter the .py files and change my location to the you like to establish the files 
1- open terminal where your project is located
run the setup_env.bat

2- download the data
run download_data.bat file that are located inside the "Scripts" folder

3- Set Up the Pub/Sub Emulator
run start_emulator.py in the terminal

4- Build the Docker image with the following command:
docker build -t movies-etl-image .

5- run the docker container
docker run -d --name movies-etl-container -p 8085:8085 movies-etl-image

6- create topic and subscription by python
run the foolowing command on terminal
- navigate to where your environment located and then get into the folder create_topic_subsribtion.py and run the following code:
(venv) D:\DEPI Data Engineer\0_projects\ETL_MOVIES\venv\Scripts>py create_topic_subscription.py

7- run publish_test_message.py to test data ingestion for the actual data ingestion next step.

8- run process_data.py to extract the CSVs files

9- run preprocessing_data.py to preprocess the data

10- make a folder in the container to copy the data in (run this line code in new terminal)
- open docker
- click on 3 dots
- open terminal of the your container
- run the code below
mkdir -p /data

11- run the publish_data.py to send data to the container we have made
