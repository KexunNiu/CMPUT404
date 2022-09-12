import requests

#print the requests version
print(requests.__version__)

#GET https://www.google.com/
getGoogle = requests.get("https://www.google.com/")
print(getGoogle.status_code)

#print the script from raw url itself
getGitRaw = requests.get("https://raw.githubusercontent.com/KexunNiu/CMPUT404/main/Lab1/Lab1.py")
print(getGitRaw.text)