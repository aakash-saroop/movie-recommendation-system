from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import requests
import random

raw_data = pd.read_csv("/Users/aakashsaroop/Desktop/Netflix/movie_titles.csv", error_bad_lines=False)

print(raw_data.shape)
print(raw_data.head())

raw_data = raw_data.to_numpy()
print(raw_data.shape)
print(raw_data[:10,:])
print("No. of movie not able to read from csv:",17770-raw_data.shape[0])
print(type(raw_data[0][2]))
imdb_ratings = np.zeros((raw_data.shape[0]+1, 3))

# The first movie has been made as the column name
# The movie is 'Dinosaur Planet'
# Its imdb rating is 7.7
# It has 438 ratings

imdb_ratings[0][0] = 1
imdb_ratings[0][1] = 7.7
imdb_ratings[0][2] = 438
url = 'https://www.google.com/search?ei=dr0xYOPtM72W4-EPnKKryAw&q=imdb+'
ratings_not_found = 0
ten_random_indices = np.random.randint(49, size=(10, 1))

    #print(imdb_ratings[x,:])
#print("No. of ratings not found and taken as -1",ratings_not_found)

for x in range(raw_data.shape[0]):

    print("Iteration:",x+1, "\tRatings not found",ratings_not_found)
    imdb_ratings[x+1][0] = raw_data[x][0]
    year = int(raw_data[x][1])

    url2 = url + raw_data[x][2] + " "+str(year)
    req = requests.get(url2)
    s = BeautifulSoup(req.text, "html.parser")

    links = s.find_all('a')
    
    for link in links:
        y = re.findall("(<a .*imdb.com.*</a>)",str(link))
        if(y!=[]):
            break
    if(y==None):
        link = '-1'
        #imdb_ratings[x+1][1] = '-1'
        imdb_ratings[x+1][1] = -1
        imdb_ratings[x+1][2] = -1
        ratings_not_found+=1
        continue


    #imdb_ratings[x+1][1] = imdb_link
    #print(imdb_ratings[x+1][1])
    try:
        link_parts = str(link).split('/')

        imdb_link = "http://"+link_parts[3]+'/'+link_parts[4]+'/'+link_parts[5]+'/'
        url3 = imdb_link
        req2 = requests.get(url3)
        s2 = BeautifulSoup(req2.text, "html.parser")
        rating_class = s2.find('div',{'class':"ratingValue"})
        if rating_class ==None:
            imdb_ratings[x+1][1] = -1
            imdb_ratings[x+1][2] = -1
            ratings_not_found+=1
            continue
        title = rating_class.find('strong')
        title = str(title)
        strong_title_sentence = re.findall("<strong title=(.*)>",title)
        rating_and_no_users = re.findall("([0-9.]+)",strong_title_sentence[0])
        imdb_ratings[x+1][1] = float(rating_and_no_users[len(rating_and_no_users)-1])
        if len(rating_and_no_users)==3:
            imdb_ratings[x+1][2] = float(rating_and_no_users[len(rating_and_no_users)-2])
        else:
            imdb_ratings[x+1][2] = int(rating_and_no_users[len(rating_and_no_users)-3]+rating_and_no_users[len(rating_and_no_users)-2])
    except:
        imdb_ratings[x+1][1] = -1
        imdb_ratings[x+1][2] = -1
        ratings_not_found+=1

#Save to CSV File


np.savetxt("imdb1.csv", imdb_ratings, delimiter=",")
for x in ten_random_indices:
    print(x, imdb_ratings[int(x),:])
