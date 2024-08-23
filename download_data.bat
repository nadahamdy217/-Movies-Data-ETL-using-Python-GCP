@echo off
REM Create the data directory if it doesn't exist
if not exist "..\data" mkdir ..\data

echo Downloading MovieLens dataset...
curl -o ..\data\ml-100k.zip https://files.grouplens.org/datasets/movielens/ml-100k.zip
echo Unzipping dataset...
powershell -command "Expand-Archive -Path '..\data\ml-100k.zip' -DestinationPath '..\data\'"
echo Data download and extraction complete.
