#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "546643485-WaT1mm4EwJe2RrnxMk5xfNxiUxnvfHc3HQgk6jFO"
access_token_secret = "GbaChVqU98h8NpUQ1FzfSG2AonWFBVdtalv5d9LNDfUrU"
consumer_key = "Orgmlwvc3OVi8UtyB1Idk1ArM"
consumer_secret = "GItv17P5pNOqtf2eRnjpfTTyuveo4LoCHUw4OZz3HJtEOo7i7p"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

#This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])