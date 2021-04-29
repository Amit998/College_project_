from logging import addLevelName
import keys
import sys
import tweepy

class TwitterData:
    searchUser=None
    currentUserName=None
    searchedUserName=None
    searchedUserDescription=None
    searchedUserLocation=None
    searchedFollowers=None
    searchedUserFollowing=0
    api=None
    
    def __init__(self,username="AmitDut34462253"):
        self.currentUserName=username
        # self.set_UserInfo(username)
        
    
    def isCurrentUser(self,name):
        if self.currentUserName == name:
            return True
        return False

    def twiteer_auth(self):
        try:
            consumer_key=keys.API_KEY
            consumer_secret_key=keys.API_SECRET_KEY
            access_token=keys.ACCESS_TOKEN
            access_token_secret=keys.ACCESS_TOKEN_SECRET
        except KeyError:
            sys.stderr.write("TWITTER_* enviorment variable not set")
            sys.exit(1)
        auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
        auth.set_access_token(access_token,access_token_secret)
        self.api=tweepy.API(auth,wait_on_rate_limit=True)
        api=tweepy.API(auth,wait_on_rate_limit=True)
        return api
    def get_followers(self):
        # print(self.searchedFollowers)
        for follower in self.searchedFollowers():
            print(follower.name)
    

    def add_description(self,desc):
        # api=self.twiteer_auth()
        self.api.update_profile(description=desc)
    
    def my_recent_tweet(self):
        tweets=self.api.home_timeline(count=1)
        tweet=tweets[0]
        print(f"Liking tweet {tweet.id} of {tweet.author.name}")
        
    
    def get_Twitter_Client(self):
        self.api=self.twiteer_auth()
    
    def set_UserInfo(self,name):
        api=self.twiteer_auth()
        # print(addLevelName)
        user=api.get_user(name)

        self.searchedUserName=user.name
        self.searchedFollowers=user.followers
        self.searchedUserDescription=user.description
        self.searchedUserLocation=user.location
    

    def get_searched_UserInfo(self):
        return self.searchedUserName,self.searchedUserDescription,self.searchedUserLocation


    def search_tweet(self,topic):
        for tweet in self.api.search(q=topic, lang="en", rpp=10):
            print(f"{tweet.user.name}:{tweet.text}")
            print('\n')
    
    def search_user(self,name):
        self.set_UserInfo(name)
        # print(self.get_searched_UserInfo())
    
    def top_trending(self):
        trends_result = self.api.trends_place(1)
        # print(trends_result)
        for trend in trends_result[0]["trends"]:
            print(trend["name"])

    def test(self):
        print(self.currentUserName)

        # print("lol")

TW=TwitterData()
# TW.test()
TW.search_user("MarcusMergulhao")
# TW.get_followers()
# TW.add_description("Hi")
# TW.search_tweet(topic="FC Goa")
TW.top_trending()
#FEATURES TO BE ADDED