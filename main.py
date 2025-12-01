import os
from flask import Flask, jsonify
from src.website import website
from src.data_manager import get_sav_data
import configparser

# Gestion del Ini
config = configparser.ConfigParser()
config.read('user_data.ini')

sav_route = config['Config']['sav_route']
sav_gen = int(config['Config']['sav_gen'])

# Gestion del Flask
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
    return jsonify(
        get_sav_data(sav_route, sav_gen)
        )

#L
def main():
    port = int(os.environ.get('PORT', 80))
    app.run(port=port)

if __name__ == "__main__":
    main()
