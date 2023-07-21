from bs4 import BeautifulSoup
import requests


#year = input("what your would you like to go back to(YYYY-MM-DD)")

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

songs = soup.find_all("div", class_="o-chart-results-list-row-container")
a = soup.find("span", class_="c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet")
b = soup.find_all("h3", id="title-of-a-story")
ranking = []
song_name = []
for song in songs:
    #ranking.append(song.find("span", class_="c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet").getText().split())
    rank = (song.find("span",
                             class_="c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet").getText()).split()
    song_name.append(song.find("h3", id="title-of-a-story").getText().strip())
    ranking.append(int(int(rank[0])))
