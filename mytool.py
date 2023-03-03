                                                                                                                      mytool.py                                                                                                                        Modified
import requests

print("Get the source of website")
url = input("Enter a URL: ")
response = requests.get(url)

print(response.text)
