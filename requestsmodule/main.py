import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.status_code)
print(r.text)


data = r.json()
print(data)
print(data["title"])

params = {"userId" : 1}
r = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)


headers ={
    "Authorization": "bearer mytoken",
    "User-agent": "LogAnalyzer/1.0"
}

r = requests.get("https://example.com/api", headers=headers)
print(r)
