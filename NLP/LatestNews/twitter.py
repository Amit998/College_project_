import keys
import sys,tweepy

def twitter_auth():
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
    api=tweepy.API(auth,wait_on_rate_limit=True)
    return auth,api

# auth=twitter_auth()
# api.update_status("Look, I'm tweeting from #Python using twitter")

def get_twitter_client():
    auth,api=twitter_auth()
    client=tweepy.API(auth,wait_on_rate_limit=True)
    timeline=api.home_timeline()

    for tweet in timeline:
        print(tweet.user.name)
        print(tweet.text)
    # print(timeline.use)
    # client=auth.get_user("MarcusMergulhao")
    # return client


if __name__=="__main__":
    # user=input("Enter Username:- ")
    client=get_twitter_client()
    # client.update_status("Hello")
    # for status in tweepy.Cursor(client.home_timeline,screen_name=user).items(1):
    #     print(status.text)

    for _ in  tweepy.Cursor(client.search,q=user,lang="en").items(10):
        print(_.text)
        print("\n")
    # api=get_twitter_client()
    # user = api.get_user("ElonMusk")
    # print(user)
    # print("User details:")
    # print(user.name)
    # print(user.description)
    # print(user.location)
    # api.update_profile(description="I like Python")
    # for follower in user.followers():
        # print(follower.name)


