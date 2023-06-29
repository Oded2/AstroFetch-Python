import os
import json


def enterToContinue():
    input("Press ENTER to continue ")


def check_file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.isfile(file_path)


api_key = input("Enter your API key here ")

with open("params.json", 'w') as f:
    with open("settings.json", 'r') as j:
        content = json.load(j)
        content["thumbs"] = True
        content["api_key"] = api_key
    json.dump(content, f, indent=6)

if check_file_exists("images", "placeholder.txt"):
    os.remove(os.path.join("images", "placeholder.txt"))

print("Setup finished")
enterToContinue()
