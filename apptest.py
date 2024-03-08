import os
import requests
import hashlib

def parse_and_create_files():
    # Fetch data from the Flask application
    url = "http://localhost:5000/data"
    response = requests.get(url)
    data = response.json()

    # Create 'files' sub-directory if it doesn't exist
    if not os.path.exists('files'):
        os.makedirs('files')

    # Iterate over samples and create files
    for sample in data['samples']:
        name = sample['name']
        file_id = sample['id']
        file_path = os.path.join('files', f"{file_id}.txt")

        # Write name to the file
        with open(file_path, 'w') as file:
            file.write(name)

        # Calculate SHA256 sum of the file contents
        with open(file_path, 'rb') as file:
            file_contents = file.read()
            sha256_hash = hashlib.sha256(file_contents).hexdigest()

        # Verify SHA256 sum matches the file id
        if sha256_hash == file_id:
            print(f"File '{file_path}' created successfully.")
        else:
            print(f"Error: SHA256 sum of file '{file_path}' does not match the file id.")

if __name__ == "__main__":
    parse_and_create_files()
