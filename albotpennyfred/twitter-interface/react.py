

def analyze(data):
    try:
        content = data["text"]
    except (TypeError, KeyError) as e:
        print("Error on_data: %s" % str(e))
        return True
    if "weather" in content:
        # call function to deliver weather response
    elif "remind" in content:
        # call function to post response later
    elif "when" in content and "leave" in content:
        # call function to get directions
    else:
        # return "sry didnt understand lol"
    return True
