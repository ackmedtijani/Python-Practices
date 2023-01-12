import feedparser 
import nltk

url = ""
llog = feedparser.parse("{}".format(url))
entries = llog.entries
post = entries[3]
title = post.title

content = post.content[2].value
tokens = nltk.tokenize(nltk.clean_html(content))
print(tokens)
