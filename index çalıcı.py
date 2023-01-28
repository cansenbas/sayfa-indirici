import requests

url = "https://www.senbas.com"

response = requests.get(url)

with open("example.html", "w") as file:
    file.write(response.text)