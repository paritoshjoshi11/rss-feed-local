import feedparser
from pprint import pformat

response = feedparser.parse('https://medium.com/feed/tag/life')
data=response.entries[0]

print(data.keys())
print(pformat(data))