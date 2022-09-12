import requests

#print the requests version
print(requests.__version__)

#GET https://www.google.com/
getGoogle = requests.get("https://www.google.com/")
print(getGoogle.status_code)