import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.w3schools.com/python/python_inheritance.asp'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and print the title of the page
    title = soup.title
    print("Title of the page:", title.text)

    # Extract and print the text inside the <h1> tag
    heading = soup.find('h1')
    print("Heading:", heading.text)

    # Extract and print the text inside the <p> tag
    paragraph = soup.find('p')
    print("Paragraph:", paragraph.text)

    # Extract and print the text inside all <li> tags
    list_items = soup.find_all('li')
    print("List Items:")
    for item in list_items:
        print("-", item.text)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
