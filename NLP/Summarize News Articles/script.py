from textblob import TextBlob
from newspaper import Article
from  csv import writer



class Article_Reading:
    link=None
    url=None
    article=None
    analysis=None
    PharseText=None
    file_name='data/saved_article.csv'

    def __init__(self,url):
        self.url=url
        self.article = Article(self.url)
        self.article.download()
        self.article.parse()
        self.article.nlp()
        self.ParseText=TextBlob(self.article.text)
        
    def analize_total_text(self):
        self.analysis=TextBlob(self.article.text)
        print(self.analysis.polarity)
    
    def analize_by_sentence(self):
        for sentence in self.ParseText.sentences:
            print(sentence)
    

    def get_article_title(self):
        print(self.article.title)

        return self.article.title
    
    def get_article_author(self):
        print(self.article.authors)

        return self.article.authors
    
    def get_article_date(self):
        print(self.article.publish_date)

        return self.article.publish_date
    
    def get_article_summary(self):
        print(self.article.summary)

        return self.article.summary

    
    def get_article_tags(self):
        print(self.article.tags)

        return self.article.tags
    
    def save_article(self):
        from string import punctuation

        # print(punctuation)

        punctuation=list(punctuation)
        punctuation.append('\n')
        
        # for sent in self.ParseText:
            # print(sent)
        test=self.ParseText.split(' ')
        print(test)

        # tokens=[ token for token in self.ParseText if token not in punctuation ]

        # print(tokens)

        # punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~''\“\”/'

        # for sentence in self.ParseText.sentences:
        #     for ele in sentence:
        #         if ele in punc:
        #             sentence=sentence.replace(ele,"")
        # print(sentence)


        


        # row_contents=[f"{self.get_article_title()}",f"{self.get_article_author()}",f"{self.get_article_date()}",f"{self.get_article_summary()}",f"{self.get_article_tags()}"]

        # with open(self.file_name,'a+',newline='') as  write_obj:

        #     csv_writter=writer(write_obj)

        #     csv_writter.writerow(row_contents)


        # print(row_contents)
        
        pass

    
   



    


    
    def test(self):
        print("hello")


url = 'https://www.thehindu.com/news/national/covid-like-pandemics-can-pose-threat-to-countrys-internal-security-says-ghulam-nabi-azad/article33250461.ece'


ar=Article_Reading(url)

# ar.analize_text()
# ar.analize_by_sentence()
# ar.get_article_title()
ar.save_article()
