import requests
import json
import os


def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension


def check_file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.isfile(file_path)


def enterToContinue():
    input("Press ENTER to continue")


url = "https://api.nasa.gov/planetary/apod"

with open("params.json", 'r') as f:
    params = json.load(f)

response = requests.get(url, params=params, timeout=30)

if not response.status_code == 200:
    if response.status_code == 403:
        print("Invalid API key, please visit https://api.nasa.gov/ and register for one")
    else:
        print("Error:", response.status_code)

    exit()
data = response.json()
with open("test/test.json", 'w') as f:
    json.dump(data, f, indent=6)
for i in range(len(data)):

    title = data[i]["title"]

    image_url = data[i]["url"]
    image_extension = get_file_extension(image_url)
    print(f"Processing image: {title}")
    new_response = requests.get(image_url)
    file_name = f"{title}{image_extension}"
    print(file_name)
    if not check_file_exists("images", f"{file_name}"):

        with open(f"images/{file_name}", 'wb') as f:
            f.write(new_response.content)
    else:
        print(title + " already exists")

print("Operation Finished")
