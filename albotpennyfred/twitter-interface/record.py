import requests


def record(data):
    try:
        log = {"id": data["id"], "username": data["user"]["screen_name"],
               "text": data["text"], "time": data["created_at"]}
        requests.post("http://127.0.0.1:8000/record_log/", log)
    except ConnectionError:
        print("ConnectionError: failed to establish a connection")
