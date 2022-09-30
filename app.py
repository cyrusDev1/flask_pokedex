from flask import Flask, render_template
from pokemon import *
from liveserver import LiveServer
import requests

app = Flask(__name__)

ls = LiveServer(app)

@app.route('/')
def home():
    pokemons = asyncio.run(all_pokemon())
    return ls.render_template('index.html', pokemons=pokemons)
