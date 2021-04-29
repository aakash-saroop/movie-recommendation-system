import urllib.request, urllib.parse, urllib.error
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
def movie_summary(name):
    #name = name.split(" ").join("+")
    url = "https://www.google.com/search?q=imdb"+name
    req = requests.get(url)
    s = BeautifulSoup(req.text, "html.parser")

    links = s.find_all('a')
    for link in links:
        y = re.findall("(<a .*imdb.com.*</a>)",str(link))
        if (y!=[]):
            break

    if (y==None):
        link = '-1'


    link_parts = str(link).split('/')

    imdb_link = "http://"+link_parts[3]+'/'+link_parts[4]+'/'+link_parts[5]+'/'
    url3 = imdb_link

    req2 = requests.get(url3)
    s2 = BeautifulSoup(req2.text, "html.parser")
      #<div class="ipc-html-content ipc-html-content--base"><div>
      #              Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.
      #      </div></div>
    summary_class = s2.find_all('div',{'class':"summary_text"})
    summary_class = summary_class[0]
    summary_text = str(summary_class)
    #print(type(summary_text))
    #print(summary_text)
    summary_text = re.findall("(.*)", summary_text)
    return(summary_text[2].strip())
#description = .find_all('div')
#print(description)'''
name = input("Enter name of the movie")
print(movie_summary(name))
