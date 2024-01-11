import requests


#Similar reference files: Urllib.py and Urrlib2.py. Contains urllib module

#Easily make hppt requests to get information from websites
#NB: requests module is great for getting info from websites, but isn't great for parsing those info,
#better to use beautifulsoup for parsing.


#STATUS CODE & VALUES
#1. 200         Response OK
#2. 300         Redirect
#3  400         Client error (Trying to access a website you are not authorized to)
#4  500         Server error


#urlTest = "https://www.google.com"
urlTest = 'https://xkcd.com/353/'
response = requests.get(urlTest)
#response = requests.get('https://www.behance.net/ibrahimsuleiman3', auth=('user', 'pass'))  #Requires login details
print(f'THE STATUS CODE: {response.status_code}')       #Returns response code
print(response.ok)      #Returns true(<400 status code) or false(400 or 500 status code). Check for only client & server error (main focus)
print(f'THE REQUEST HEADERS: {response.headers}')

print('\n\n')
print(f'RESPONSE VALUE: {response.text}')                #Returns text content of the website in unicode(html,css...)


#Download images from website, use content (returns content in byte)
UrlImage = "https://imgs.xkcd.com/comics/python.png"
response1 = requests.get(UrlImage)
print(f'IMAGE IN BINARY:\n {response1.content}')    #Save in a file to be able to view
with open('Internet3.png', 'wb') as f:
    f.write(response1.content)

