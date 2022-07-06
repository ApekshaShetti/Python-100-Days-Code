from bs4 import BeautifulSoup
import requests 
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID='99ed42577881444cb358e99c74602896'
SPOTIPY_CLIENT_SECRET='ae9c29c45f5845d1bc6d0725fcbf6c82'
URL = "https://www.billboard.com/charts/hot-100/"
user = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        # redirect_uri="http://example.com",
        redirect_uri="https://example.com/callback",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
        ))


response = requests.get(URL+user)
data = response.text

soup = BeautifulSoup(data,'html.parser')
# songs = soup.find_all("span", class_="chart-element__information__song")
songs = soup.find_all(name="h3", class_="a-no-trucate")
print(songs)

user_id = sp.current_user()["id"]
song_names = [song.getText() for song in songs]


song_uris = []
year = user.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



playlist = sp.user_playlist_create(user=user_id, name=f"{user} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)