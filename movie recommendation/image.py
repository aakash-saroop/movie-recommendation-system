import random
import urllib.request
import imdb
import psycopg2
from flask_mail import Mail


from flask_mail import Message

import smtplib

sender = 'bhairavn10@gmail.com'
receivers = ['bhairavn10@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")

# ia=imdb.IMDb()
# index()
# top = ia.get_top250_movies()

# def download_image(url):
#     name = random.randrange(1,100)
#     fullname = str(name)+".jpg"
#     urllib.request.urlretrieve(url,fullname)     


# con = psycopg2.connect(
#     host = "127.0.0.1",
#     database = "movierecommender",
#     user = "postgres",
#     password = "admin",
#     port="5432")

# cur=con.cursor()


# print()
# # print("hello")
# # print (ia.get_movie(top[0].movieID).data['cover url'])
# import urllib.request
# j=int(0)
# # for i in top:
# #     # print(i['title'],type(i['year']),type(str(i['rating'])))
# #     st='assets/images/' + str(j) + '.jpg'
# #     # a=ia.get_movie(i.movieID).data['genres']
# #     # print(a)
# #     cur.execute("INSERT INTO public.moviedatabase (title,year,rating,image) VALUES (%s,%s::bigint,%s,%s)",(i['title'],i['year'],i['rating'],st));
# #     con.commit()
# #     j+=1
# #     print(j)
# cur.execute("select * from public.moviedatabase")
# mdata = cur.fetchall()
# for i in mdata:
#     print(i)
# # print(top[0]['genres'])
#     # st="images/"+str(i)+".jpg"
#     # urllib.request.urlretrieve(ia.get_movie(top[i].movieID).data['cover url'], st)
#     # print(j)
#     # j+=1
#     # print(lst[],"\n")
#     # print(top[1]['title'])
#     # print ("title: %s year: %s" % (movie['title'], movie['year']))
#     # print ("Cover url: %s" % movie['cover url'])
# # download_image("http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg")
# 									<img src="{{ url_for('static',filename='{{j[3]}}')}}" class="img-fluid" alt="">
