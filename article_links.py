import requests
from bs4 import BeautifulSoup, NavigableString, Tag

pages = 240
links = []

# Iterate through each link by iterating through each of 240 pages
for page in range(1, pages+1):
    # Connect to the website
    response = requests.get('https://www.inklingsnews.com/category/b/page/' + str(page) + '/', verify=False)
    response = response.text.strip() # Receive HTML

    soup = BeautifulSoup(response)
    anchors = soup.find_all('a') # parse all anchor tags in the HTML

    for a in anchors:
        if "https://www.inklingsnews.com/b" in a['href'] and a['href'] not in links:
            links.append(a['href'])
    

open('links.txt', 'w').close()
with open('links.txt', 'w') as file:
    for link in links:
        file.write(link + "\n")
