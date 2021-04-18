import pandas as pd
import numpy as np
import re
import requests
import random
import  bs4
from bs4 import BeautifulSoup

raw_data = pd.read_csv("/Users/aakashsaroop/Desktop/Netflix/movie_titles.csv", error_bad_lines=False, encoding = "ISO-8859-1")

print(raw_data.shape)
print(raw_data.head())

raw_data = raw_data.to_numpy()
print(raw_data.shape)
print(raw_data[:10,:])
print("No. of movie not able to read from csv:",17770-raw_data.shape[0])

img = np.zeros((raw_data.shape[0]+1, 2), dtype=object)

img[0][0] = 1
img[0][1] = 'https://m.media-amazon.com/images/M/MV5BNTY2MDk5ODE0OV5BMl5BanBnXkFtZTcwNTMxNzQyMQ@@._V1_UY268_CR20,0,182,268_AL__QL50.jpg'
not_found = 0

url = 'https://www.google.com/search?ei=dr0xYOPtM72W4-EPnKKryAw&q=imdb+'

for x in range(raw_data.shape[0]):
    if (x<=15001):
      continue
    if (x%1000==1):
      np.savetxt("img"+str(x)+".csv", img, delimiter=",",fmt='%s')
    if (x%100==1):
      print("Iteration:",x+1, "\tnot found",not_found)
      print(img[x][0], img[x][1])
    img[x+1][0] = raw_data[x][0]
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
        img[x+1][1] = '-1'
        not_found+=1
        continue

      link_parts = str(link).split('/')

      imdb_link = "http://"+link_parts[3]+'/'+link_parts[4]+'/'+link_parts[5]+'/'
      url3 = imdb_link

      req2 = requests.get(url3)
      s2 = BeautifulSoup(req2.text, "html.parser")

      poster_class = s2.find('div',{'class':"poster"})
      link = poster_class.find('img').get('src')
      link = str(link)
      img[x+1][1] = link


    except:
      link = '-1'
      not_found+=1
      img[x+1][1] = '-1'

np.savetxt("img.csv", img, delimiter=",",fmt='%s')

for x in ten_random_indices:
    print(x, imdb_ratings[int(x),:])
