from webbrowser import get
from flask import Flask, render_template
from pokemon import *
from liveserver import LiveServer
import requests

app = Flask(__name__)

ls = LiveServer(app)
pokemons = asyncio.run(all_pokemon())

@app.route('/')
def home():
    return ls.render_template('index.html', pokemons=pokemons)

@app.route('/pokedex/<int:id>')
def pokedex(id):
    url_desc = pokemons[1].get("species").get('url')
    desc = asyncio.run(one_pokedex(url_desc))
    one_pokemon = {}
    one_pokemon['image'] = pokemons[id].get("sprites").get("front_default")
    one_pokemon['description'] = desc.get("flavor_text_entries")[1].get("flavor_text")
    return ls.render_template('pokedex.html', one_pokemon=one_pokemon)
