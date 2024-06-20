import requests
from PIL import Image
import io
import pandas as pd
import os

# Directory to cache images
cache_directory = "items"
os.makedirs(cache_directory, exist_ok=True)

# Read the CSV file
df = pd.read_csv("Erc1155_info.csv")

for index, row in df.iterrows():
    image_url = row['Image URL']
    id_value = row['ID']
    file_name = f"{id_value}.png"
    file_path = os.path.join(cache_directory, file_name)

    if not os.path.exists(file_path):
        # If the image is not in the cache, download and save it
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))
        image.save(file_path)
        print(f"Image file {file_name} downloaded and cached.")
    else:
        # If the image is in the cache, load it from there
        image = Image.open(file_path)
        print(f"Image file {file_name} loaded from cache.")

print("All image files downloaded and cached successfully.")
