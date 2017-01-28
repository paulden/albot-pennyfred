import requests


def analyze(data):
    try:
        content = data["text"]
        username = (data["user"]["screen_name"], data["user"]["name"])
        place = data["place"]
        if "weather" in content:
            return answer_weather(content, username)
            print("on donne le temps")
        elif "remind" in content:
            # call function to post response later
            pass
        elif "when" in content and "leave" in content:
            # call function to get directions
            pass
        else:
            # return "sry didnt understand lol"
            pass
    except (TypeError, KeyError) as e:
        print("Error on_data: %s" % str(e))
        pass


def answer_weather(content, username):
    # TODO: Parse location in content to get appropriate weather from API
    answer = "@%s Dear %s, " % username
    r = requests.get("http://127.0.0.1:8000/weather/brussels")
    weather = r.json()
    temp = round(weather["temperature"])
    desc = weather["desc"]
    location = weather["location"]
    answer += "expect a %s in %s today, with about %i°C. Have a good day" % (desc, location, temp)
    return answer


def answer_directions(data, username):
    return True


