# auth_server.py
from flask import Flask, redirect, request, jsonify
import os, urllib.parse, base64, requests
from dotenv import load_dotenv
import json

load_dotenv()  # reads .env in same folder

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI", "http://127.0.0.1:27228/spotify_callback")
SCOPE = "user-read-email user-read-private playlist-read-private playlist-modify-private playlist-modify-public user-library-read user-library-modify"

app = Flask(__name__)

@app.route("/authorize")
def authorize():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "state": "state123",  # optional, for CSRF protection in prod change to random
        "show_dialog": "true"
    }
    url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
    return redirect(url)

@app.route("/spotify_callback")
def spotify_callback():
    error = request.args.get("error")
    if error:
        return f"Error from Spotify: {error}", 400

    code = request.args.get("code")
    if not code:
        return "No code received", 400

    # Exchange code for access token
    token_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    resp = requests.post(token_url, data=data, headers=headers)
    if resp.status_code != 200:
        return f"Token exchange failed: {resp.status_code} {resp.text}", 500

    token_data = resp.json()
    # Save tokens locally (tokens.json) and print to console
    with open("tokens.json", "w") as f:
        json.dump(token_data, f, indent=2)

    print("TOKENS RECEIVED:\n", json.dumps(token_data, indent=2))
    return (
        "<h2>Authorized ✅</h2>"
        "<p>Tokens saved to <code>tokens.json</code> in this folder.</p>"
        "<p>Check terminal for access_token and refresh_token.</p>"
    )

if __name__ == "__main__":
    # bind explicitly to 127.0.0.1 to satisfy Spotify loopback rules
    app.run(host="127.0.0.1", port=27228, debug=False)
