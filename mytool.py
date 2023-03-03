import requests

Print("Get the source of website")
url = input("Enter a URL: ")
response = requests.get(url)

print(response.text)
