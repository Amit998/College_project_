import spacy
from  spacy.lang.en.stop_words import  STOP_WORDS
from string import punctuation
from heapq import nlargest
stopWords=list(STOP_WORDS)
nlp=spacy.load('en_core_web_sm')


def tokenize(text):
    docs=nlp(text)
    tokens=[ token.text for token in docs ]


    punctuation=list(punctuation)
    punctuation.append('\n')
    tokens=[ token for token in tokens if token not in punctuation ]

    return tokens

def word_frequencey_couter(docs):
    word_frequency={}
    for word in docs:
        if word.text.lower() not in stopWords:
            if (word.text.lower() not in punctuation ):
                if word.text not in word_frequency.keys():
                    word_frequency[word.text] = 1
                else:
                    word_frequency[word.text] +=1
    
    max_frequency=max(word_frequency.values())    

    for word in word_frequency.keys():
        word_frequency[word]=word_frequency[word]/max_frequency
    
    return word_frequency,max_frequency


def sentence_tokenize(docs,word_frequency):
    
    sentence_score={}
    sentence_tokens=[sent for sent in docs.sents]
    for sent in sentence_tokens:
        for word in sent:
            if (word.text.lower() in word_frequency.keys()):
                if(sent not in sentence_score.keys()):
                    sentence_score[sent]=word_frequency[word.text.lower()]
                else:
                    sentence_score[sent] +=word_frequency[word.text.lower()]
    return sentence_tokens,sentence_score
    

def summarize_text(text,size):
    sentence_tokens,sentence_score=sentence_tokenize()
    select_length=int(len(sentence_tokens) * size)
    get_summary=nlargest(select_length,sentence_score,key=sentence_score.get)
    final_summary=[word.text for word in get_summary]
    summary=' '.join(final_summary)

    return summary







text="""Interesting aspect here is, election or no election, money laundering activities are showing an upward trend in India. The official data till 30 April 2013 available with indiatoday.in shows money laundering has increased significantly every year, over the past few years.

The number of money laundering investigations increased from 798 on 31 December 2009 to 1405 on 15 December 2011, to 1510 on 31 August 2012, to 1530 on 30 November 2012, and 1561 on 30 April 2013. Even prosecution cases have increased.  "From 2009 to 2013, more than 1500 cases of money laundering have come before us, out of that 65 per cent cases are trade-based money laundering," a senior DRI officer said.

Trade-Based Money Laundering (TBML) is not a new but very lethal form of money laundering, which the Government of India is finding very difficult to plug.

The Financial Action Task Force (FATF) has recognised misuse of the trade system as the main method (about 65 per cent) by which criminal organisations and terrorist financiers move money for the purpose of disguising their origins and integrating with the formal economy.

These are legitimate commercial transactions to camouflage laundering activities. "TBML has been growing as an alternative remittance system that allows illegal and unaccounted money with an opportunity to earn and move the proceeds disguised as legitimate trade, " a revenue officials says.

The basic techniques of TBML include: trade mispricing (over and under-invoicing of goods amd services), split invoicing (multi-level/multiple invoicing on single consignment of goods and services), quantity manipulation (over and under shipment of goods and services), mis-description (mis-declaration of goods of import/export) and concealment (contraband in cover cargo).

The main method which is being used to conduct TBML is by influencing government policy to suit particular interests, use of front companies and using the banking system to launder money by indulging in a complex web of transactions to conceal the real source of income.

"Our conservative estimate suggests undervaluation to the tune of Rs 2000 crore per annum on electronic goods is taking place. Not only that due to overvaluation of import, estimated loss to exchequer is to the tune of Rs 900 crore in last two years," one DRI official says.

The recent modus operandi includes - circular trading in gold/diamond jewellery, where consignment is imported from Hong Kong/Dubai, then processing and reshuffling of jewels between consignment of overseas and Special Economic Zones is done (which takes more than a month). Later, shift to jewellery from diamond because of reduction of buyer credit period of 90 days (as per RBI norms). Buyer credit used to open fixed deposit account in banks to make profit out of interest arbitrage.

"When non-shell companies are used, a commission of 0.1 percent of the value of transaction is paid. Profits are laundered to safe havens," DRI official said. According to DRI, AEL group is one such company which laundered money to the tune of Rs 49,000 crore via this modus operandi, against which, showcause notices have been sent and investigation is still on.

Even the Enforcement Directorate (ED) has sent a few showcause notices to IT companies suspecting TBML. Senior ED officials also admit that TBML cases are on the rise and they are keeping a close tab on it.

Now, investigating officers have raised an alarm on increasing TBML in the country. An officer says, "Due to rising TBML, country is losing revenue, parallel economy of black money is working on ground and damaging the financial institutions. Unfortunately, our enforcement agencies are also ill-equipped to curb it."

Revenue officials have sought strong penal measures, streamlining of multiple export incentives schemes, special fast track economic offence courts, an integrated approach towards TBML, and international cooperation.
"""
size=0.3

tokenize(text,size)


