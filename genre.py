import urllib.request, urllib.parse, urllib.error
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
'''def stream_link(movie_name):
    url = 'https://www.google.com/search?ei=dr0xYOPtM72W4-EPnKKryAw&q=imdb+'
    # Type name of the movie/ tv series which you want to search



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
    subtext_class = s2.find('div',{'class':"subtext"})
    genres = subtext_class.find_all('a')
    print(genres)
    return genres
movie_name = input()
print(stream_link(movie_name))'''
raw_data = pd.read_csv("/Users/aakashsaroop/Desktop/Netflix/movie_titles.csv", error_bad_lines=False, encoding = "ISO-8859-1")
raw_data = raw_data.to_numpy()
genres = np.zeros((raw_data.shape[0]+1, 2), dtype=object)
genres[0][0] = 1
genres[0][1] = 'Documentary+Animation+Family'
not_found = 0

url = 'https://www.google.com/search?ei=dr0xYOPtM72W4-EPnKKryAw&q=imdb+'
for x in range(raw_data.shape[0]):
    #if (x<=16001):
    #  continue

    if (x%1000==1):
      np.savetxt("genre"+str(x)+".csv", genres, delimiter=",",fmt='%s')
    if (x%100==1):
      print("Iteration:",x+1, "\tnot found",not_found)
      print(genres[x][0], genres[x][1])
    genres[x+1][0] = raw_data[x][0]
    try:
      year = int(raw_data[x][1])
    except:
      year = ""
    try:
      name = raw_data[x][2].replace(' ','+')
      url2 = url + name + "+"+str(year)

      req = requests.get(url2)
      s = BeautifulSoup(req.text, "html.parser")

      links = s.find_all('a')

      for link in links:
        y = re.findall("(<a .*imdb.com.*</a>)",str(link))
        if (y!=[]):
          break

      if (y==None):
        link = '-1'
        genres[x+1][1] = '-1'
        not_found+=1
        continue

      link_parts = str(link).split('/')

      imdb_link = "http://"+link_parts[3]+'/'+link_parts[4]+'/'+link_parts[5]+'/'
      url3 = imdb_link

      req2 = requests.get(url3)
      s2 = BeautifulSoup(req2.text, "html.parser")

      subtext_class = s2.find('div',{'class':"subtext"})

      lst_genres_links = subtext_class.find_all('a')
      lst_genres = []
      for lst_genre_link in lst_genres_links:
          lst_genres.append(lst_genre_link.getText())
      lst_genres = lst_genres[:len(lst_genres)-1]
      str_genres = ""
      for lst_genre in lst_genres:
          str_genres = str_genres+lst_genre+"+"
      str_genres = str_genres[:len(str_genres)-1]
      #print(str_genres)
      genres[x+1][1] = str_genres


    except:
      link = '-1'
      not_found+=1
      genres[x+1][1] = '-1'
np.savetxt("genre.csv", genres, delimiter=",")
