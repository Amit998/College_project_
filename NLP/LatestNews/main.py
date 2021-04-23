from googlesearch import search
import requests



class Info_Getter_From_Google():
    News_Channels=["NDTV","Times Now","CNN-News18","WION"]
    links=[]
    topic=None
    # results=search("Narendra Modi Times Now")
    

    def __init__(self,topic):
        self.topic=topic

    def internet_connectivity(self):
        url = "http://www.google.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            return "200"
        except (requests.ConnectionError, requests.Timeout) as exception:
            return "NoInternet"

        

    
    def get_tweet(self):
        pass

    def wiki_details(self):
        pass
    def news_articles(self):
        # self.internet_connectivity()
        for news_link in self.News_Channels:
            temp_Str=f"{self.topic} {news_link}"
            print(temp_Str)
            results=search(temp_Str)

            print(results[0])
    
    def test(self):
        status=self.internet_connectivity()
        if (status=="200"):
            print("Go")
        else:
            print("No Internet")
        # temp_str=requests.get('https://www.wionews.com/india-news/cyclone-amphan-pm-modi-visits-west-bengal-announces-immediate-relief-of-rs-1000-crore-300359')
        # print(temp_str.text)
        pass
        
topic="Narendra Modi"
ifg=Info_Getter_From_Google(topic)
# ifg.news_articles()
ifg.test()