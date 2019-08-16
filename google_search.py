#https://python-googlesearch.readthedocs.io/en/latest/

from googlesearch import search
for url in search('your query', stop=5):
    print(url)
