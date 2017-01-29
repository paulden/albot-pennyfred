import requests
import time
from geotext import GeoText
import datefinder
from keys import *


def analyze(data):
    try:
        content = data["text"]
        username = (data["user"]["screen_name"], data["user"]["name"])
        place = data["place"]
        if "weather" in content:
            city = GeoText(content).cities[0]
            return answer_weather(city, username)
        elif "remind" in content:
            datetime = parse_time(content)
            task = parse_task(content)
            return answer_reminder(data["id"], datetime, task, username)
        elif "how long" in content:
            city = GeoText(content).cities[0]
            return answer_directions(place, city, username)
        else:
            # return "sry didnt understand lol"
            pass
    except (TypeError, KeyError) as e:
        print("Error on_data: %s" % str(e))
        pass


def answer_weather(city, username):
    answer = "@%s Dear %s, " % username
    r = requests.get("http://127.0.0.1:8000/weather/" + city)
    weather = r.json()
    temp = round(weather["temperature"])
    desc = weather["desc"]
    location = weather["location"]
    answer += "expect %s in %s today, with about %i°C. Have a good day" % (desc, location, temp)
    return answer


def answer_directions(place, city, username):
    answer = "@%s Dear %s, " % username
    if "name" in place:
        dest = city
        location = place["name"]  # The location provided by Twitter seems inaccurate (at least in Paris)
        r = requests.get("http://127.0.0.1:8000/directions/" + location + "/" + dest)
        duration = r.json()["duration"]
        answer += "according to Google Maps, the trip will take you %s by car. Please, drive safely." % duration
    else:
        answer += "you seem to have disabled the location in your tweets, I cannot help you unfortunately."
    return answer


def answer_reminder(tweet_id, datetime, task, username):
    answer = "@%s Very well, %s, " % username
    time_in_tweet = datetime[11:]
    timestamp = time_to_timestamp(datetime)
    answer += "I will not fail to remind you to %s at %s" % (task, time_in_tweet)
    reminder = "@%s Dear %s," % username
    reminder += "don't forget to %s, it is now high time you take care of such business!" % task
    try:
        plan = {"id": tweet_id, "username": username[0], "text": reminder,
                "plan_time": str(timestamp), "client_id": client_id}
        r = requests.post("http://127.0.0.1:8000/plan_tweet/", plan)
        if r.status_code == 201:
            return answer
        else:
            return "@%s Sorry %s, I could not make a note of that and I deeply apologized." % username
    except ConnectionError:
        print("ConnectionError: failed to establish a connection")


def time_to_timestamp(datetime):
    """
    Converts a datetime formatted as 2017/01/31 16:00 in a timestamp 1485702900.0
    to use it in Buffer (reminder task)
    """
    return time.mktime(time.strptime(datetime, '%Y-%m-%d %H:%M'))


def parse_time(content):
    """
    Tries to parse the time in the text to plan a tweet
    """
    matches = datefinder.find_dates(content)
    l = list(matches)
    print(l)
    date = str(l[0])
    return date[:-3]


def parse_task(content):
    """
    Tries to parse the task in the text to reply a tweet appropriate
    This requires some improvements
    """
    matches = list(datefinder.find_dates(content, index=True))
    end_index = matches[0][1][0]
    start_index = content.find("emind me to")
    if start_index >= 0:
        return content[start_index+12:end_index]
    else:
        return "that"
