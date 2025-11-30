import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from website import website
from pokemon_data import get_party_data
from Gen3Save.Gen3Save import Gen3Save

from flask import Flask, send_file, jsonify

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/")
def index():
    return website()

@app.route("/API/Game")
def api():
    return jsonify(get_party_data())

#L
def main():
    port = int(os.environ.get('PORT', 80))
    app.run(port=port)

if __name__ == "__main__":
    main()
