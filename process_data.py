import pandas as pd

# Define the path to the data files
ratings_file = 'D:/DEPI Data Engineer/0_projects/ETL_MOVIES/venv/data/ml-100k/u.data'
movies_file = 'D:/DEPI Data Engineer/0_projects/ETL_MOVIES/venv/data/ml-100k/u.item'

# Create a DataFrame for Movie Ratings
ratings = pd.read_csv(ratings_file, delimiter='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])

# Create a DataFrame for Movie Names
with open(movies_file, 'r', encoding="ISO-8859-1") as read_file:
    counter = 0
    movies_df = pd.DataFrame(columns=['item_id', 'movie_name', 'release_timestamp'])

    # Iterate through the lines in the file
    for line in read_file:
        # From each line extract the first three values
        fields = line.split('|')
        item_id, movie_name, release_timestamp = fields[0], fields[1], fields[2]
        movie_name = movie_name[0:len(movie_name) - len(' (1234)')]

        # Aggregate line data
        line_data = [int(item_id), str(movie_name), release_timestamp]

        # Create a temp DataFrame and append it to movies_df
        temp_df = pd.DataFrame(data=[line_data], columns=['item_id', 'movie_name', 'release_timestamp'])
        movies_df = pd.concat([temp_df, movies_df], ignore_index=True)

        counter += 1

    # Sort Values by item id
    movies_df.sort_values(by='item_id', ascending=True, inplace=True)

# Close file
read_file.close()

# Export to CSV
ratings.to_csv('D:/DEPI Data Engineer/0_projects/ETL_MOVIES/venv/data/ratings.csv', index=False)
movies_df.to_csv('D:/DEPI Data Engineer/0_projects/ETL_MOVIES/venv/data/movies.csv', index=False)
