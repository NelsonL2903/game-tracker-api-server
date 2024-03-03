# utils.py


def parse_search_results(results):
    return [
        dict(
            id=game.get("id"),
            name=game.get("name"),
            released=game.get("released"),
            rating=game.get("metacritic"),
            image=game.get("background_image"),
            genres=[
                genre.get("name") for genre in game.get("genres", []) if len(genre) > 0
            ],
        )
        for game in results
    ]
