import requests

try:
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout = 5)
    r.raise_for_status()
    data = r.json()
    print(data)

except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Network error")
except requests.exceptions.HTTPError as e:
    print("bad response", e)
except requests.exceptions.RequestException as e:
    print("Other request error: ", e)
