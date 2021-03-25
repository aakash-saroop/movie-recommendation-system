import imdb
from flask import Flask,render_template,request
from datetime import datetime,date

def webscrap():
    ia=imdb.IMDb()
    top = ia.get_top250_movies()
    # print(top[0])
    lst=[]
    ls = top
    j = int(0)
    for i in top:
        if j<=10:
            lst.append(i)
            j+=1
    # print(lst[],"\n")
    # print(top[1]['title'])
    # print ("title: %s year: %s" % (movie['title'], movie['year']))
    # print ("Cover url: %s" % movie['cover url'])
    return top


# lst=[]
# ls = top
# j = int(0)
# for i in top:
#     # if i['y']>=2018:

#     print(ia.get_movie(i.movieID).data['cover url'])
    

# # print ("title: %s year: %s" % (top[0]['title'], top[0]['year']))
# # print ("Cover url: %s" % top[0]['cover url'])

# # access = imdb.IMDb()
# # movie = access.get_movie(1132626)

# # print ("title: %s year: %s" % (movie['title'], movie['year']))
# # print ("Cover url: %s" % top[0]['cover url'])