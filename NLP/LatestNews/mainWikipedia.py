import wikipedia


class WIKInfo:
    wikipedia.set_lang("en")
    searchName=None
    searchNameList=[]
    first_name=None
    suggested_search_name=None
    def __init__(self,name):
        
        self.searchName=name
        self.searchNameList=wikipedia.search(self.searchName)
        self.first_name=self.searchNameList[0]
        self.suggested_search_name=wikipedia.suggest(self.first_name)
    
    def wiki_summary(self):
        summary=wikipedia.summary(self.suggested_search_name)
        print(summary)
    
    def wiki_page_data(self):
        page_data=wikipedia.page(self.suggested_search_name)
        print(wikipedia.page(self.suggested_search_name).content)
        url=wikipedia.page(self.suggested_search_name).url
        refs=wikipedia.page(self.suggested_search_name).references
        page_title=wikipedia.page(self.suggested_search_name).title
        categories=wikipedia.page(self.suggested_search_name).categories
    
    def location_search(self):
        geo_location=wikipedia.geosearch(37.787, -122.4)

    

    

    def test(self):
        pass
        # print(self.searchName)
        # print(self.suggested_search_name)
        # print(self.first_name)
       


wiki=WIKInfo("Elon Musk")
# wiki.test()
# wiki.wiki_summary()
wiki.wiki_page_data()