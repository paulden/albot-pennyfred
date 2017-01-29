from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream, API, TweepError
import json
from react import *
from record import record
from keys import *


# This is a basic listener that reacts appropriately when reading streamed tweets
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        formatted_data = json.loads(data)
        if "text" in formatted_data:
            record(formatted_data)
            if formatted_data["user"]["screen_name"] != twitter_username:
                try:
                    tweet_id = formatted_data["id"]
                    response = analyze(formatted_data)
                    if response:
                        api.update_status(response, tweet_id)
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
