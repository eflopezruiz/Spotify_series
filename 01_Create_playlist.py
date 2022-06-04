import requests
### It is necessary to refresh the Spotify Token on: 
### https://developer.spotify.com/console
### Code based on Imhad tutorial: https://github.com/imdadahad

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/loedru12/playlists'
ACCESS_TOKEN = 'BQCVvvg4cBe64cPBe2KSxy_fjr59H2xXXZzC0p_VBZg-wz7GnjZQovdZ5B6-ByDKYY_Yo7DY4LrXUBlWSrwBIxhhbO_QVNTn2NqhL8wAGGYDJr_E4nhpA9DxZ7uVyOB1XJwumTZR164Uswkd2sS0STki3XWHdGnbTffqS6ZDrX9xjFuMyoQ5pmHwPDzhlxJEex9KxXIPew'

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            'name': name,
            'public': public
        }
    )
    json_resp = response.json()
    
    return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name='Python generated playlist',
        public=False
    )
    
    print(f"Playlist: {playlist}")
    
if __name__=='__main__':
    main()