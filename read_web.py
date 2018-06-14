import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import language_check


links = []
with open('links.txt', 'r') as file:
    for line in file:
        line = line.strip()
        links.append(line)

articles = []

for link in links:
    response = requests.get(link, verify=False)
    response = response.text.strip()
    paragraph = ""
    soup = BeautifulSoup(response)
    ps = soup.find_all('p')

    article = []

    for p in ps:
        article.append(p.getText())

    articles.append(article)


import language_check

counts = []
tool = language_check.LanguageTool('en-US')

for article in articles:
    count = 0
    for p in article:
        matches = tool.check(p) # Potential errors

        for match in matches:
            count += 1

    counts.append(count)


'''moreThanFourCount = 0
with open('errorCounts.txt', 'r') as file:
    for line in file:
        n = int(line.strip())
        if n >= 10:
            moreThanFourCount += 1

print(moreThanFourCount)'''

# Write the error count of each article in a file
open('errorCounts.txt', 'w').close()
with open('errorCounts.txt', 'w') as file:
    for c in counts:
        file.write((str(c) + "\n"))

        
    
    



