# main.py

from fastapi import FastAPI
from decouple import config
import os
import requests

app = FastAPI()

@app.get("/search/{search_query}")
async def search(search_query: str):
    API_KEY = os.environ.get('RAWG_API_KEY')
    search_url = "https://api.rawg.io/api/games?key={API_KEY}&page_results=5&page=1&search={searchQuery}&search_precise=true"
    search_results = requests.get(search_url).json()
    return search_results