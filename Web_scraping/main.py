from bs4 import BeautifulSoup
import requests

import lxml

with open("website.html") as file:
    contents= file.read()

soup =BeautifulSoup(contents,"html.parser")
print(soup.title)

all_anchors =soup.find_all(name="a")
print(all_anchors)
#getting text in anchors

for tag in all_anchors:
    print(tag.getText())

#getting links in the anchors
for tag in all_anchors:
    print(tag.get("href"))


