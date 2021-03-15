import spacy
from  spacy.lang.en.stop_words import  STOP_WORDS

from heapq import nlargest



class Text_Summarization:
    stopWords=list(STOP_WORDS)
    nlp=spacy.load('en_core_web_sm')
    def __init__(self,doc,size=0.3):


        self.doc=self.nlp(doc)
        self.size=size

    def get_punctuation(self):
        from string import punctuation
        punctuation=list(punctuation)
        punctuation.append('\n')

        return punctuation

    
    def tokenize(self):
        
        docs=self.doc
        tokens=[ token.text for token in docs ]


        punctuation=self.get_punctuation()
        tokens=[ token for token in tokens if token not in punctuation ]

        return tokens

    def word_frequencey_couter(self):
        punctuation=self.get_punctuation()
        word_frequency={}
        for word in self.doc:
            if word.text.lower() not in self.stopWords:
                if (word.text.lower() not in punctuation ):
                    if word.text not in word_frequency.keys():
                        word_frequency[word.text] = 1
                    else:
                        word_frequency[word.text] +=1
        
        max_frequency=max(word_frequency.values())    

        for word in word_frequency.keys():
            word_frequency[word]=word_frequency[word]/max_frequency
        
        return word_frequency,max_frequency
    

    def sentence_tokenize(self):
        sentence_tokens=[sent for sent in self.doc.sents]
        return sentence_tokens
    
    def sentence_tokenize_score(self):
        word_frequency,_=self.word_frequencey_couter()
        sentence_tokens=self.sentence_tokenize()
    
        sentence_score={}
        
        for sent in sentence_tokens:
            for word in sent:
                if (word.text.lower() in word_frequency.keys()):
                    if(sent not in sentence_score.keys()):
                        sentence_score[sent]=word_frequency[word.text.lower()]
                    else:
                        sentence_score[sent] +=word_frequency[word.text.lower()]
        return sentence_score
    
    def summarize_text(self):

        sentence_score= self.sentence_tokenize_score()
        sentence_tokens=self.sentence_tokenize()



        select_length=int(len(sentence_tokens) * self.size)

        # print(self.size)

        get_summary=nlargest(select_length,sentence_score,key=sentence_score.get)

        # print(get_summary)

        final_summary=[word.text for word in get_summary]
        summary=' '.join(final_summary)

        return summary

        
    

    def print_text(self):
        # print(self.doc)
        # print(self.size)
        i=self.summarize_text()
        print((i))



text="""

Dalglish celebrated his 70th birthday on Wednesday and, to honour the milestone, the Dalglish family have set up the 7Appeal which will raise funds to support young families in Liverpool who urgently require baby basics.

The appeal runs until the end of the month and is a collaborative effort between the club, Red Neighbours and the Dalglish family, with the LFC Foundation facilitating fundraising.

Dalglish said: "While many other worthwhile causes have been supported during the last 12 months there is still a lot of support needed for young families, particularly pre-school-aged children and babies.

"The essentials you need for a new baby and young kids are expensive and with many suffering job losses as a result of the pandemic, it has made it near impossible for these families.

"I want to use my birthday to launch the 7Appeal and help as many families as possible."

"""
summ=Text_Summarization(text,size=0.3)
summ.print_text()