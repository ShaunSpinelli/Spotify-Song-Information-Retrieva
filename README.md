# Spotify Song Information Retrieval

This Python script utilizes the Spotipy API to extract song details (song name and artist) from a provided Spotify URL. Written in 10 min in conjunction with [ChatGPT](https://chat.openai.com/share/8ba2446c-ca22-4631-8295-79e50910eedd)

## Setup

1. Clone this repository to your local machine.

2. Install the required dependencies by running the following command: `pip install -r requirements.txt
`

3. Obtain Spotify API credentials:
 - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
 - Create a new application to obtain the client ID and client secret.
 - Create `.env` file and add `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` with your actual credentials.

  eg:

 ```env
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
 ```

4. Update `songs_urls` array with the urls of thr songs want information for.

5. Run script `python3 get_name_from_url.py`


Output:

```txt
Song: Live Your Music, Artist: Crazy White Boy, Apple Gule
Song: Fever, Artist: Lewis Thompson, Punctual, Hight
Song: One Last Dance, Artist: Audien, XIRA
```
