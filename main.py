
import json
import os


def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension


def check_file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.isfile(file_path)


def enterToContinue():
    input("Press ENTER to continue ")


def appendJSON(json1, json2):
    for i in json1:
        json2[i] = json1[i]
    return json2


try:
    import requests
except ModuleNotFoundError as error:
    print(error, "Please run 'pip3 install requests` to install the requests module.")
    enterToContinue()
    exit()
url = "https://api.nasa.gov/planetary/apod"

print("Fetching data...")
params_exist = check_file_exists("", "params.json")
if not params_exist:
    print("Please run the setup.py file in order to create the 'params.json' file")
    enterToContinue()
    exit()

with open("settings.json", 'r') as f:
    settings = json.load(f)

with open("params.json", 'r') as f:

    params = json.load(f)

params = appendJSON(params, settings)

response = requests.get(url, params=params, timeout=60)
if not response.status_code == 200:
    if response.status_code == 403:
        print("Invalid API key, please visit https://api.nasa.gov/ and register for one")
    elif response.status_code == 504:
        print("Server did not get a response in time from the upstream server that it needed in order to complete the request.")
    else:
        print("Error:")
    print("Status code:", response.status_code)
    enterToContinue()
    exit()

data = response.json()
for i in range(len(data)):

    title = data[i]["title"]
    image_url = data[i]["url"]
    if "https://www.youtube.com/embed/" in image_url:
        image_url = data[i]["thumbnail_url"]
    image_extension = get_file_extension(image_url)
    print(f"Processing image: {title}")
    new_response = requests.get(image_url)

    file_name = f"{title}{image_extension}".replace(":", "")

    if not check_file_exists("images", f"{file_name}"):

        with open(f"images/{file_name}", 'wb') as f:
            f.write(new_response.content)
    else:
        print(title + " already exists")

print("Operation Finished")
enterToContinue()
