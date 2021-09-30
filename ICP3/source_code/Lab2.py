# Using beautiful soup
import requests
from bs4 import BeautifulSoup

# Setup and access webpage
response = requests.get(url= "https://en.wikipedia.org/wiki/Deep_learning")

soup =BeautifulSoup(response.content, "html.parser")

# Find title by heading
title = soup.find(id="firstHeading")
print(title.string)

# Create holder for all links
links = []
# For line with 'a'
for link in soup.find_all('a'):
    # Add the text under href aka the link
    links.append(link.get('href'))
# Create a writable txt for storage
f = open('link_data.txt', 'w+')
# Write title of page first
f.write(title.string)

# Run thorugh all the links and write them to file one per line
for i in range(len(links)):
    if links[i] != None:
        f.write("\n")
        f.write(links[i])
# Close the file       
f.close()

