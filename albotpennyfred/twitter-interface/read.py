from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream, API, TweepError
import requests
import json
from react import *


# Variables that contains the user credentials to access Twitter API
access_token = "804056756842332161-EWcJaRS0Cu1TWqzQ9dIVObICTDwnsMH"
access_token_secret = "eixQsXjTCt2W7dgpBHIf6MhkyegaIUvwyXDzKnTObjzUi"
consumer_key = "CeUYVK9tVB6bKzZ6lEMYRZXf7"
consumer_secret = "sfzWreSXVeL38C5tfM4HGONtLOo1h2OW4pUSm800dVdtxtvMLM"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        formatted_data = json.loads(data)
        if "text" in formatted_data:
            if formatted_data["user"]["screen_name"] != "il_m0nco":
                try:
                    tweet_id = formatted_data["id"]
                    api.update_status(analyze(formatted_data), tweet_id)
                except (TweepError, KeyError) as e:
                    print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    api = API(auth)

    stream.userstream()
    print("Streaming de data en cours...")
