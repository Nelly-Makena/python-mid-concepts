import requests
from bs4 import BeautifulSoup

movies = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(movies.content, "html.parser")
titles =soup.find_all(name="h3")

titles_text = [title.get_text(strip=True) for title in titles]


with open("movies.txt", "w") as file:
    for title in reversed(titles_text):
        file.write(title + "\n")