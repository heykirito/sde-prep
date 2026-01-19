import time 
import requests


def fetch_data():
    try:
        r = requests.get("https://jsonplaceholde.typicode.com/posts", timeout = 5)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Failed to fetch posts", e)
        return []
