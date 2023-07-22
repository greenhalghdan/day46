from bs4 import BeautifulSoup
import requests
import spotipy
from setuptools._distutils.command.clean import clean
from spotipy import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import os

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
YEAR = input("what your would you like to go back to(YYYY-MM-DD)")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{YEAR}")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

songs = soup.find_all("div", class_="o-chart-results-list-row-container")
ranking = []
song_name = []
song_uris = []
for song in songs:
    #ranking.append(song.find("span", class_="c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet").getText().split())
    # rank = (song.find("span",
    #                          class_="c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet").getText()).split()
    song_name.append(song.find("h3", id="title-of-a-story").getText().strip())
    # ranking.append(int(int(rank[0])))
scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

for song in song_name:
    result = sp.search(q=f"track: {song} year: {YEAR.split('-')[0]}")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{YEAR} Billboard 100", public=False)
print(playlist)
print(playlist["id"])
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)