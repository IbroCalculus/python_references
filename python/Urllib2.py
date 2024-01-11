

#Similar reference files: Urllib1.py and Requests.py. Contains urllib and requests module

#using urllib request, There's also requests module, check Internet2
from urllib import  request


#Fetch data from the internet
response = request.urlopen("https://www.google.com")
print(response)     #Returns a response
print(f'STATUS CODE IS: {response.getcode()}')

#STATUS CODE & VALUES
#1. 200         Response OK
#2. 300         Redirect
#3  400         Client error (Trying to access a website you are not authorized to)
#4  500         Server error

#Read data from the website
response = request.urlopen("https://www.google.com")
print(f'READ DATA: {response.read()}')