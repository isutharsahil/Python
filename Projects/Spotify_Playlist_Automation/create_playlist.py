import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load tokens from auth_server
with open("tokens.json") as f:
    tokens = json.load(f)

access_token = tokens["access_token"]

# Create Spotify client
sp = spotipy.Spotify(auth=access_token)

# Get current user
user = sp.current_user()
user_id = user['id']
print(f"Logged in as: {user['display_name']} ({user_id})")

# Playlist info
playlist_name = "Fein!"
playlist_desc = "Created via Python + Spotipy"
track_ids_to_add = ["2p8IUWQDrpjuFltbdgLOag", "7fBv7CLKzipRk6EC6TWHOB", "42VsgItocQwOQC3XWZ8JNA"]  # Replace with your track IDs, <not albums & collectons id only track id>

# Step 1: Check if playlist exists
existing_playlists = sp.current_user_playlists(limit=50)['items']
playlist = None
for pl in existing_playlists:
    if pl['name'] == playlist_name:
        playlist = pl
        break

# Step 2: Create playlist if it doesn't exist
if not playlist:
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=True,
        description=playlist_desc
    )
    print(f"Playlist created: {playlist['name']} (id: {playlist['id']})")
else:
    print(f"Playlist already exists: {playlist['name']} (id: {playlist['id']})")

# Step 3: Get existing track IDs in the playlist
existing_tracks = []
offset = 0
while True:
    results = sp.playlist_items(playlist['id'], fields='items.track.id,total', limit=100, offset=offset, additional_types=['track'])
    if not results['items']:
        break
    for item in results['items']:
        if item['track']:
            existing_tracks.append(item['track']['id'])
    offset += len(results['items'])

# Step 4: Filter only new tracks
new_tracks = [tid for tid in track_ids_to_add if tid not in existing_tracks]

# Step 5: Add new tracks if any
if new_tracks:
    sp.playlist_add_items(playlist['id'], new_tracks)
    print(f"Added {len(new_tracks)} new track(s) to playlist.")
else:
    print("No new tracks to add. Playlist is up-to-date.")
