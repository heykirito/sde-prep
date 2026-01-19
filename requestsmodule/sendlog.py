import requests
import time

entry = {
    "date": "2026-01-12",
    "time": "10:00:00",
    "level": "ERROR",
    "message": "Disk full"
}



def send_log(entry: dict):
    try:
        r = requests.post(
            "https://httpbin.org/post",
            json=entry,
            timeout=5
        )
        r.raise_for_status()
        print("Sent log successfully")
    except requests.exceptions.RequestException as e:
        print("Failed to send log", e)

send_log(entry)

def get_with_retry(url, retries=1):
    for attempt in range(1, retries+1):
        try:
            print(f"Attempt {attempt}")
            r =  requests.get(url, timeout=5)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Failed", e)
            if attempt == retries:
                raise

            time.sleep(2)

get_with_retry("https://httpbin.org/post")
