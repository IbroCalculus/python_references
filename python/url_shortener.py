import pyshorteners

# Prompt the user to enter a URL
link_URL = input("Enter the URL: ")

try:
    # Initialize the shortener
    shortener = pyshorteners.Shortener()

    # Shorten the URL using TinyURL
    short_URL = shortener.tinyurl.short(link_URL)

    # Print the shortened URL
    print(f'The shortened URL is: {short_URL}')
except Exception as e:
    # Handle exceptions
    print(f"An error occurred: {e}")
