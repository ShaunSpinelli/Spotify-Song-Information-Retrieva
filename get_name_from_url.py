import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

# Replace these placeholders with your own Spotify API credentials
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Initialize Spotipy with client credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_info(url):
    # Extracting track ID from the URL
    track_id = url.split('/')[-1].split('?')[0]
    
    # Get track details using Spotipy
    track_info = sp.track(track_id)
    
    # Extract song name and artists' names
    song_name = track_info['name']
    artists = ", ".join([artist['name'] for artist in track_info['artists']])
    
    return {'Song': song_name, 'Artist': artists}


songs_urls = [
    'https://open.spotify.com/track/53NvpLMBXRS203Z4c1Gs6d?si=fe97ae43b0e74883',
    'https://open.spotify.com/track/3D3fw7H4zK3S6prSBncAkt?si=64997c017ea040f6',
    'https://open.spotify.com/track/1nV6VafLPuRSsXgbDY3i6L?si=b74a38a3e6da4123'
    
] 

for url in songs_urls:
    # Get song information
    song_info = get_song_info(url)

    # Display the song name and artist
    print(f"Song: {song_info['Song']}, Artist: {song_info['Artist']}")
