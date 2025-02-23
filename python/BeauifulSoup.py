import requests
from bs4 import BeautifulSoup   # pip install beautifulsoup4

# URL of the website
url = 'http://quotes.toscrape.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quote elements
    quotes = soup.find_all('div', class_='quote')

    # Extract and print each quote and its author
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f'"{text}" - {author}')
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")