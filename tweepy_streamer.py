from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials
#   #   #   TWITTER AUTHENTICATOR   #   #   #
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

#   #   #   TWITTER STREAMER    #   #   #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets
    """
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    ## We will save the tweets to the "fetched_tweet_filename"
    ## instead of tweets just appearing on the terminal
    ## For filtering the tweets we can use a "hash_tag_list"
    def stream_tweets(self, fetched_tweets_filename, has_tag_list):
        # This handles Twitter authetication and the connection to
        # the Twitter Streaming API
            listener = TwitterListener(fetched_tweets_filename)
            auth = self.twitter_authenticator.authenticate_twitter_app()
            stream = Stream(auth, listener)
            stream.filter(track=hash_tag_list)

#Class to print the tweets
#The class inherits from the "StreamListener" class

class TwitterListener(StreamListener):
    """
    Basic listener class that just prints recieved tweets to stdout
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    ## over-riding on_data method
    def on_data(self, data):
        try:
            print(data)
            ## We will append the tweets as we stream them to the
            ## "fetched_tweets_filename"
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except  BaseException as e:
            print("Error on data: %s" % str(e))
        return True


    ## over-riding on_error method
    def on_error(self, status):
        print(status)

## Creating Object from "StdOutListener" class
if __name__ == "__main__":
    hash_tag_list = ['donald trump', 'hillary clinton', 'barack obama', 'bernine sanders']
    fetched_tweets_filename = "tweets.json"

    ## Define TwitterStreamer object
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
