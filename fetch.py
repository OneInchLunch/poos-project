import os
import requests

def fetch_weights(url, destination):
    if not os.path.exists(destination):
        print("Downloading weights file, the server is slow so this could take a few minutes.")
        response = requests.get(url)

        if response.status_code == 200:
            with open(destination, 'wb') as file:
                file.write(response.content)
            print("Weights file downloaded successfully.")
        else:
            print(f"Failed to download the weights file. Status code: {response.status_code}")
    else:
        print("Weights file already exists. Skipping download.")
