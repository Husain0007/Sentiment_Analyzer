from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

#Class to print the tweets
#The class inherits from the "StreamListener" class

class StdOutListener(StreamListener):
    ## over-riding on_data method
    def on_data(self, data):
        print(data)
        return True
    ## over-riding on_error method
    def on_error(self, status):
        print(status)

## Creating Object from "StdOutListener" class
if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
    stream.filter(track=['donald trump', 'hillary clinton', 'bernie sanders', 'barank obama'])
    