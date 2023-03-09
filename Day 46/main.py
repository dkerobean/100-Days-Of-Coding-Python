from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "http://example.com",
        client_id = os.getenv("CLIENT_ID"),
        client_secret = os.getenv("CLIENT_SECRET"),
        show_dialog = True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

user_date = input("Wic year do you want to travel to? Type the date in this format YYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + user_date)
chart = response.text

soup = BeautifulSoup(chart, "html.parser")
song_titles = soup.find_all(name="h3", id="title-of-a-story")

song_names = [songs.getText() for songs in song_titles]
print(song_names)

song_uris = []
year = user_date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


