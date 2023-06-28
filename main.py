import requests


def enterToContinue():
    input("Press ENTER to ")


url = "https://api.nasa.gov/planetary/apod"


api_key = "RH5e6AJeKi4RfZo11EoRbhCwlGspTA2Cdc6nZgoG"
# api_key = "RH5e6AJeKi4RfZo11EoRbhCwlGspTA2Cdc6nZ"

# day = input("Enter Day ")
# month = input("Enter Month ")
# year = input("Enter Year ")

# date = f"{year}-{month}-{day}"
# print(date)
params = {
    "date": "2022-8-1",
    "api_key": api_key

}


response = requests.get(url, params=params)
print(response.url)

if not response.status_code == 200:
    if response.status_code == 403:
        print("Invalid API key, please visit https://api.nasa.gov/ and register for one")
    else:
        print("Error:", response.status_code)

    exit()
data = response.json()

# Extract the required information
title = data["title"]
explanation = data["explanation"]
image_url = data["url"]

# Do something with the data
print("Title:", title)
new_response = requests.get(image_url)
with open(f"images/{title}.jpg", 'wb') as f:
    f.write(new_response.content)
