import pandas as pd
import os
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# Define paths for the existing files
ratings_csv_path = r'D:\DEPI Data Engineer\0_projects\ETL_MOVIES\venv\data\ratings.csv'
movies_csv_path = r'D:\DEPI Data Engineer\0_projects\ETL_MOVIES\venv\data\movies.csv'
merged_csv_path = r'D:\DEPI Data Engineer\0_projects\ETL_MOVIES\venv\data\full_data.csv'

# Load the datasets into DataFrames
ratings_df = pd.read_csv(ratings_csv_path)
movies_df = pd.read_csv(movies_csv_path)

full_data = pd.merge(ratings_df, movies_df, on='item_id')

# Save the merged DataFrame to a new CSV file
full_data.head(10)
full_data = full_data.sort_values(by='item_id', ascending=True)
full_data

# data preprocessing   
### 1st step: check data:
#see missing values and column types
full_data.info()
#noticed that column release_timestamp has null values
# Percentage of missing values in release_timestamp
missing_percentage = full_data['release_timestamp'].isnull().mean() * 100
print(f"Missing percentage: {missing_percentage:.2f}%")

#There will be no problems with dropping them but I want to  fill them with the most common value.
mode_timestamp = full_data['release_timestamp'].mode()[0]
full_data['release_timestamp'].fillna(mode_timestamp, inplace=True)
print(full_data['release_timestamp'].isnull().sum())
#now there is no missig values for this column
# Check outliers for each column expxect item_id
# check outliers for each column

def detect_outliers(data, column):
    z_scores = np.abs(stats.zscore(data[column]))
    return np.where(z_scores > 3)


# box plot for each column for rates

sns.boxplot(x=full_data['rating'])
##### no outliers in ratings column

#Detect Outliers in 'timestamp' column and 'release_timestamp' column
#handle both columns
# Convert 'timestamp' to datetime
full_data['timestamp'] = pd.to_datetime(full_data['timestamp'], unit='s')

# Convert 'release_timestamp' to datetime
full_data['release_timestamp'] = pd.to_datetime(full_data['release_timestamp'], format='%d-%b-%Y')

full_data

# Extract 'datestamp' and 'time' from 'datetime'

full_data['datestamp'] = full_data['timestamp'].dt.date
full_data['time'] = full_data['timestamp'].dt.time

# Drop the original 'datetime' column if needed
full_data = full_data.drop(columns=['timestamp'])

full_data.head(5)
# Compare 'timestamp' and 'release_timestamp'
invalid_rows = full_data[full_data['datestamp'] < full_data['release_timestamp']]
invalid_rows
#extract unique values from movie_name is the list of invalid_rows

unique_invalid_movies = invalid_rows['movie_name'].unique()
unique_invalid_movies

#barchar the rate of unique_invalid_movies

plt.figure(figsize=(15, 5))
sns.countplot(x=invalid_rows['movie_name'])
plt.xticks(rotation=90, fontsize=8)
plt.show()
#Concluded that the most film has ratings before its release was 'Apt Pupil' -> horror and crime category
#We can conclude that these films are rated before its release depending on the advertisement of the movie itself.
#no need to clean this data.
# Check Duplicates
#check duplicate with ignore to column item_id
len(full_data[full_data.duplicated()])

#no data duplication detected

#save the full_data file after preprocessing
full_data.to_csv(merged_csv_path, index=False)
