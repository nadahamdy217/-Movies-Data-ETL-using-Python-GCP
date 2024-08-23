import subprocess

# Paths for the files and Docker container
file_path = r'D:\DEPI Data Engineer\0_projects\ETL_MOVIES\venv\data\full_data.csv'
container_id = '54fea1529a3c1360e7a9be6f5711b34b7cf6cb05955e99cba5aa59ffd1e6c95b'
container_path = '/data/full_data.csv'

def copy_to_container(file_path, container_id, container_path):
    try:
        # Use Docker cp to copy the file to the container
        result = subprocess.run(['docker', 'cp', file_path, f'{container_id}:{container_path}'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the copy operation was successful
        if result.returncode == 0:
            print(f"Successfully copied {file_path} to {container_id}:{container_path}")
        else:
            print(f"Error copying file: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Exception occurred: {e}")
        return False

# Copy the CSV file to the Docker container
copy_to_container(file_path, container_id, container_path)
s