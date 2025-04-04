import sys
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL, timeout=30)

if response.status_code != 200:
    sys.exit()

soup = BeautifulSoup(response.text, "html.parser")

titles = [title.string for title in soup.find_all(name="h3", class_="title")]
titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in titles:
        file.write(movie + "\n")
