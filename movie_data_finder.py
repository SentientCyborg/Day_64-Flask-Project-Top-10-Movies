import os
import requests

# Environment variable
MOVIE_DB_TOKEN = os.environ.get("MOVIE_DB_TOKEN")


class MovieDataFinder:
    """A class to make API calls to TMDB"""
    def __init__(self):
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {MOVIE_DB_TOKEN}",
        }

    def find_movies(self, movie_name: str) -> dict:
        """Uses the search 'movie' method on TMDB"""
        endpoint = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
        my_movie = {"query": f"{movie_name}"}
        response = requests.get(endpoint, headers=self.headers, params=my_movie).json()
        return response["results"]
