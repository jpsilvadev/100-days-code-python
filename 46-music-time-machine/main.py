import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

BILLBOARD_HOT100_ENDPOINT = " https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")


def get_billboard_date():
    wanted_date = input(
        "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
    )
    return wanted_date


def scrape_billboard(date):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
    full_url = BILLBOARD_HOT100_ENDPOINT + date
    response = requests.get(full_url, headers=header, timeout=30)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    track_titles = [
        title.getText().replace("\n", "").replace("\t", "")
        for title in soup.select("li ul li h3", class_="c-title")
    ]
    track_artist = [
        artist.getText().replace("\n", "").replace("\t", "")
        for artist in soup.select("li ul li span.c-label")
        if not artist.getText().strip().isdigit() and artist.getText(strip=True) != "-"
    ]

    tracks = zip(track_titles, track_artist)
    return list(tracks)


def main():
    date = get_billboard_date()
    tracks = scrape_billboard(date)

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_SECRET,
            scope="playlist-modify-private",
            redirect_uri="https://example.com",
            show_dialog=True,
            cache_path="token.txt",
            username=SPOTIFY_USERNAME,
        )
    )

    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)
    playlist_id = playlist["id"]

    track_uris = []
    for track in tracks:
        query = f"track:{track[0]} artist:{track[1]}"
        result = sp.search(query, type="track", limit=1)
        if not result["tracks"]["items"]:
            print(f"Track not found: {track[0]} by {track[1]}")
            continue
        print(result)
        track_uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(track_uri)

    sp.playlist_add_items(playlist_id, track_uris)


if __name__ == "__main__":
    main()
