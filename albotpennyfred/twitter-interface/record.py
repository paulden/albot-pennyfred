import requests


def record(data):
    log = {}
    log["id"] = data["id"]
    log["username"] = data["user"]["screen_name"]
    log["text"] = data["text"]
    log["time"] = data["created_at"]
    r = requests.post("http://127.0.0.1:8000/record_log", log)