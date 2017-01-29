import requests
import time


CLIENT_ID = "xxx"


def analyze(data):
    try:
        content = data["text"]
        username = (data["user"]["screen_name"], data["user"]["name"])
        place = data["place"]
        if "weather" in content:
            return answer_weather(content, username)
        elif "remind" in content:
            return answer_reminder(data["id"], content, username)
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
    answer += "expect %s in %s today, with about %i°C. Have a good day" % (desc, location, temp)
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


def answer_reminder(tweet_id, content, username):
    # TODO: Parse time and eventually tasks to get appropriate response from API
    answer = "@%s Very well, %s, " % username
    time = "4pm"
    formatted_time = "2017/01/31 16:00"
    timestamp = time_to_timestamp(formatted_time)
    task = "clean the house"
    answer += "I will not fail to remind you to %s at %s" % (task, time)
    reminder = "@%s Dear %s," % username
    reminder += "don't forget to %s, it is now high time you take care of such business!" % task
    try:
        plan = {"id": tweet_id, "username": username[0], "text": reminder,
                "plan_time": str(timestamp), "client_id": CLIENT_ID}
        r = requests.post("http://127.0.0.1:8000/plan_tweet/", plan)
        if r.status_code == 201:
            return answer
        else:
            return "@%s Sorry %s, I could not make a note of that and I deeply apologized."
    except ConnectionError:
        print("ConnectionError: failed to establish a connection")


def time_to_timestamp(datetime):
    """
    Converts a datetime formatted as 2017/01/31 16:00 in a timestamp 1485702900.0
    to use it in Buffer (reminder task)
    """
    return time.mktime(time.strptime(datetime, '%Y/%m/%d %H:%M'))
