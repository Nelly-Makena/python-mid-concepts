import requests
from bs4 import BeautifulSoup

yc_web_page = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(yc_web_page.content, "html.parser")
print(soup.title)


article_tag = soup.find(name="a",class_="storylink")#inspect the website to get the class used
article_text =article_tag.getText()
article_link = article_tag.get("href")

article_upvote = soup.find(name="span", class_="score").getText()
