from flask import Flask, render_template, request
import requests
import api_integration


spotify = api_integration.Client(api_integration.CLIENT_ID, api_integration.CLIENT_SECRET)
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        artist_info = spotify.get_random_artist()
        return render_template('result.html', artist_name=artist_info['artists']['items'][0]['name'],
         spotify_link=artist_info['artists']['items'][0]['external_urls']['spotify'])
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
