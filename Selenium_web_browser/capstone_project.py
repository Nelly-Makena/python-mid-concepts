DOCS ="https://docs.google.com/forms/d/e/1FAIpQLSeu74zfwPXL2I3EjvldumM3xgK12FQtcFvUcXHBAZz88psqUw/viewform?usp=sf_link"
import requests
from bs4 import BeautifulSoup

property_listings = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(property_listings.content, "html.parser")

# Use the correct class name by inspecting the element on the webpage
titles = soup.find_all("a", class_="list-card-link")

# Initialize the list
title_list = []

# Extract href and append to list
for title in titles:
    href = title.get("href")
    title_list.append(href)

# Print the list
print(title_list)


