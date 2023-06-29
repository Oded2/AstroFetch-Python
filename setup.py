import json


def enterToContinue():
    input("Press ENTER to continue ")





api_key = input("Enter your API key here ")

with open("params.json", 'w') as f:
    with open("settings.json", 'r') as j:
        content = json.load(j)
        content["thumbs"] = True
        content["api_key"] = api_key
    json.dump(content, f, indent=6)

print("Setup finished")
enterToContinue()
