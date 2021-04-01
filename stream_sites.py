import urllib.request, urllib.parse, urllib.error
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
url = 'https://www.google.com/search?ei=dr0xYOPtM72W4-EPnKKryAw&q=imdb+'
# Type name of the movie/ tv series which you want to search
movie_name = 'friends'

url2 = url+movie_name
req = requests.get(url2)
s = BeautifulSoup(req.text, "html.parser")

links = s.find_all('a')
for link in links:
        y = re.findall("(<a .*imdb.com.*</a>)",str(link))
        if(y!=[]):
            break
link_parts = str(link).split('/')

imdb_link = "http://"+link_parts[3]+'/'+link_parts[4]+'/'+link_parts[5]+'/'
url3 = imdb_link
req2 = requests.get(url3)
s2 = BeautifulSoup(req2.text, "html.parser")
rating_class = s2.find('div',{'class':"buybox buybox--default buybox--desktop"})
title = rating_class.find('a').get('href')
title = str(title)
print(title)
