import wikipedia
import wikipediaapi

print(wikipedia.summary("Elon Musk"))
wiki_wiki = wikipediaapi.Wikipedia('en')

# page_py = wiki_wiki.page('Elon Musk)')

# print(page_py)

# wiki_wiki = wikipediaapi.Wikipedia('en')
# page_py = wiki_wiki.page('Python_(programming_language)')
# print("Page - Title: %s" % page_py.title)
# # Page - Title: Python (programming language)

# print("Page - Summary: %s" % page_py.summary[0:60])
# Page - Summary: Python is a widely used high-level programming language for
# result = wikipedia.summary("India", sentences = 2)
# print(result)

# importing the module
# import wikipedia
  
# # setting language to hindi
# wikipedia.set_lang("beng")
  
# # printing the summary
# print(wikipedia.summary("India"))