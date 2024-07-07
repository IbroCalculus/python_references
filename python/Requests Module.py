import requests

#Similar reference files: Urllib.py and Urrlib2.py. Contains urllib module

#NB: requests module is great for getting info from websites, but isn't great for parsing those info,
#better to use beautifulsoup for parsing.


# #urlTest = "https://www.google.com"
# urlTest = 'https://xkcd.com/353/'
# response = requests.get(urlTest)
# #response = requests.get('https://www.behance.net/ibrahimsuleiman3', auth=('user', 'pass'))  #Requires login details
# print(f'THE STATUS CODE: {response.status_code}')       #Returns response code
# print(response.ok)      #Returns true(<400 status code) or false(400 or 500 status code). Check for only client & server error (main focus)
# print(f'THE REQUEST HEADERS: {response.headers}')
#
# print('\n\n')
# print(f'RESPONSE VALUE: {response.text}')                #Returns text content of the website in unicode(html,css...)
#



# =========== GET REQUEST =================
# url1 = r"https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url1)
# # if response.status_code == 200:
# if response.status_code == requests.codes.ok:
#     # print(f"RESPONSE HEADERS: {response.headers}")            # Get Headers
#     # print(f"RESPONSE TEXT: {response.text}")                  # Get Text
#     # print(f"URL: {response.url}")                             # Get URL
#     data = response.json()                               # Returns a python dictionary
#     # print(f"JSON RESPONSE: {data}")
#     for item in data:
#         print(f"ID: {item['id']} -> Title: {item['title']}")


# --------- Get request ---------
# response = requests.get(f"{https://httpbin.org/get")
# print(response.json())

# ------- Ger request with query parameter ---------
# paramss = {
#     "name": "John",
#     "age": "36"
# }
# # response = requests.get("https://httpbin.org/get?name=Mike&age=25")
# response = requests.get("https://httpbin.org/get", params=paramss)
# print(f"GET-URL: {response.url}")
# res_json = response.json()
# print(res_json)


# ========= POST REQUEST ============
# payload = {
#     "name": "John",
#     "age": "36"
# }
# response = requests.post("https://httpbin.org/post", data=payload)
# print(f"POST-URL: {response.url}")
# res_json = response.json()
# print(res_json)

# ======= USER AGENT ========
# User agent is an identifier in the header that tells the API what software you are using to trying to access it. A custom user agent might be added
response = requests.get("https://httpbin.org/user-agent")
print(f"USER AGENT: {response.text}")

# --- Change the value of user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get("https://httpbin.org/user-agent", headers=headers)
print(f"USER AGENT: {response.text}")

# ========= IMAGES and FILE TYPES ==========
# #Download images from website, use content (returns content in byte)
UrlImage = "https://imgs.xkcd.com/comics/python.png"
response1 = requests.get(UrlImage)
print(f'IMAGE IN BINARY:\n {response1.content}')    #Save in a file to be able to view
with open('Internet3.png', 'wb') as f:
    f.write(response1.content)

# =========== REQUEST TIMEOUT =================
try:
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts", timeout=1)   # Timeout in seconds
    print(f"RETREIVED: {response.json()}")
except Exception as e:
    print("A timeout error occurred!")