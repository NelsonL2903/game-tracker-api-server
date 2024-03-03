# main.py

from fastapi import FastAPI
from decouple import config
import requests
from utils import parse_search_results

app = FastAPI()


@app.get("/search/{search_query}")
async def search(search_query: str):
    API_KEY = config("RAWG_API_KEY")
    search_url = f"https://api.rawg.io/api/games?key={API_KEY}&page_results=5&page=1&search={search_query}&search_precise=true"
    search_results = requests.get(search_url).json().get("results")
    parsed_search_results = parse_search_results(search_results)
    return parsed_search_results
