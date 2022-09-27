#!/usr/bin/python3
import requests
import aiohttp
import asyncio

async def pokemon(session, url):
    async with session.get(url) as response:
        pokemon = await response.json()
        return pokemon

async def all_pokemon():
    async with aiohttp.ClientSession() as session:
        task = []
        for id in range(1, 12):
            url = f"https://pokeapi.co/api/v2/pokemon/{id}"
            task.append(asyncio.ensure_future(pokemon(session, url)))
        original_pokemon = await asyncio.gather(*task)
        return(original_pokemon)
