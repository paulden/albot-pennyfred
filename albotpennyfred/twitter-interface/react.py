import requests


def analyze(data):
    try:
        content = data["text"]
        username = (data["user"]["screen_name"], data["user"]["name"])
        place = data["place"]
        if "weather" in content:
            return answer_weather(content, username)
        elif "remind" in content:
            # call function to post response later
            pass
        elif "when" in content and "leave" in content:
            return answer_directions(place, content, username)
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


def answer_directions(place, content, username):
    # TODO: Parse destination in content to get appropriate time from API
    answer = "@%s Dear %s, " % username
    if "name" in place:
        dest = "Brussels"
        location = place["name"]  # The location provided by Twitter seems inaccurate (at least in Paris)
        r = requests.get("http://127.0.0.1:8000/directions/" + location + "/" + dest)
        duration = r.json()["duration"]
        answer += "according to Google Maps, the trip will take you %s by car. Please, drive safely." % duration
    else:
        answer += "you seem to have disabled the location in your tweets, I cannot help you unfortunately."
    return answer