# utils.py


def parse_search_results(result):
    return {
        "id": result["id"],
        "name": result["name"],
        "released": result["released"],
        "rating": result["metacritic"],
        "image": result["background_image"],
        "genres": [genre["name"] for genre in result["genres"]],
    }
