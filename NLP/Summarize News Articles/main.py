import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# nltk.download('punkt')

url = 'https://www.thehindu.com/news/national/covid-like-pandemics-can-pose-threat-to-countrys-internal-security-says-ghulam-nabi-azad/article33250461.ece'
article = Article(url)
article.download()
article.parse()
article.nlp()

 

print(f'Title : {article.title}')
print(f' Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f' Summary: {article.summary}')
print(f'Tags:  {article.tags}')


analysis=TextBlob(article.text)
# # print(analysis.polarity)
# print(f'Sentiment : { "Positive" if analysis.polarity > 0 else "Negetive" if analysis.polarity < 0 else "Neutral" } ')

def summarize():
    uText.get('1.0',"end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state="normal")
    alabel.config(state="normal")
    dlabel.config(state="normal")
    slabel.config(state="normal")
    tlabel.config(state="normal")
    sentimentLabel.config(state="normal")

    title.delete('1.0','end')
    title.insert('1.0',article.title)


    alabel.delete('1.0','end')
    alabel.insert('1.0',article.authors)

    date=article.publish_date
    # print(date)
    # dlabel.delete('1.0','end')
    # dlabel.insert('1.0',"article.publish_date")

    tlabel.delete('1.0','end')
    tlabel.insert('1.0',article.tags)


    slabel.delete('1.0','end')
    slabel.insert('1.0',article.summary)

    analysis=TextBlob(article.text)

    sentiment=(f'Sentiment : { "Positive" if analysis.polarity > 0 else "Negetive" if analysis.polarity < 0 else "Neutral" } ')

    sentimentLabel.delete('1.0','end')
    sentimentLabel.delete('1.0',sentiment)





    title.config(state="disabled")
    alabel.config(state="disabled")
    dlabel.config(state="disabled")
    slabel.config(state="disabled")
    tlabel.config(state="disabled")
    sentimentLabel.config(state="disabled")


root=tk.Tk()
root.title("News Summarizer")
root.geometry('800x400')

tlabel=tk.Label(root,text="Title")
tlabel.pack()
title=tk.Text(root,height=1,width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()


alabel=tk.Label(root,text="Author")
alabel.pack()
alabel=tk.Text(root,height=1,width=140)
alabel.config(state='disabled',bg='#dddddd')
alabel.pack()


dlabel=tk.Label(root,text="Date")
dlabel.pack()
dlabel=tk.Text(root,height=1,width=140)
dlabel.config(state='disabled',bg='#dddddd')
dlabel.pack()

slabel=tk.Label(root,text="Summary")
slabel.pack()
slabel=tk.Text(root,height=5,width=140)
slabel.config(state='disabled',bg='#dddddd')
slabel.pack()


tlabel=tk.Label(root,text="Tags")
tlabel.pack()
tlabel=tk.Text(root,height=1,width=140)
tlabel.config(state='disabled',bg='#dddddd')
tlabel.pack()


sentimentLabel=tk.Label(root,text="Sentiment")
sentimentLabel.pack()
sentimentLabel=tk.Text(root,height=1,width=140)
sentimentLabel.config(state='disabled',bg='#dddddd')
sentimentLabel.pack()


uText=tk.Text(root,height=1,width=140)
uText.pack()


btn=tk.Button(root,text="Summarize",command=summarize)
btn.pack()

root.mainloop()