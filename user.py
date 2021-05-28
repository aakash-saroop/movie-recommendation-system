from flask import Flask,render_template,request,flash,session,url_for,g,redirect
from passlib.hash import sha256_crypt
import psycopg2
from math import ceil
from textanalysis import returnlabel
import re
from stream_sites import stream_link
from colab_filter import recommend
from closest_user import closest
import difflib
from summary import movie_summary

app=Flask(__name__)

con = psycopg2.connect(
    host = "127.0.0.1",
    database = "movierecommender",
    user = "postgres",
    password = "admin",
    port="5432")

cur=con.cursor()
cur.execute("select * from public.topmovies")
mdata = cur.fetchall()
n=len(mdata)
temp=mdata.copy()
nslides= n//4 +ceil((n/4)-(n//4))


cur.execute("select index,title from public.movie_database")
mdata1 = cur.fetchall()
movie_name_lst=[]
for m in mdata1:
    movie_name_lst.append([m[0],m[1]])


lst=[]
@app.route('/filter',methods=['POST','GET'])
def filter():
    
    if request.get_data().decode('utf-8').strip()=="Action":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Action", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))
        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Comedy":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Comedy", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        # return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Drama":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Drama", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))
        return redirect(url_for('index'))

    elif request.get_data().decode('utf-8').strip()=="Horror":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Horror", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))
        return redirect(url_for('index'))

    elif request.get_data().decode('utf-8').strip()=="Romance":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Romance", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      
        print(len(temp),len(mdata))

        return redirect(url_for('index'))

    elif request.get_data().decode('utf-8').strip()=="Documentry":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Documentry", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      
        print(len(temp),len(mdata))

        return redirect(url_for('index'))

    elif request.get_data().decode('utf-8').strip()=="Animation":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Animation", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

    else :
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            temp.append(mpdata[i])
            count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))   
    return render_template('index.html',posts1=mdata,posts2=temp,len=n,l=len(temp),ns=4)


@app.route('/filter2',methods=['POST','GET'])
def filter2():
    
    if request.get_data().decode('utf-8').strip()=="Action":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Action", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      
        print(len(temp),len(mdata))

        return redirect(url_for('user'))
    elif request.get_data().decode('utf-8').strip()=="Comedy":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Comedy", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))
        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Drama":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Drama", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))
        return redirect(url_for('index'))

    elif request.get_data().decode('utf-8').strip()=="Horror":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Horror", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      
        print(len(temp),len(mdata))

        return redirect(url_for('index'))

    elif request.get_data().decode('utf-8').strip()=="Romance":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Romance", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      
        print(len(temp),len(mdata))

        return redirect(url_for('index'))

    elif request.get_data().decode('utf-8').strip()=="Documentry":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Documentry", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

    elif request.get_data().decode('utf-8').strip()=="Animation":
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            try:
                txt = mpdata[i][5]
            except:
                txt="Mnan"
            x = re.findall("Animation", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

    else :
        print("**",request.get_data().decode('utf-8'))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            temp.append(mpdata[i])
            count+=1      

        print(len(temp),len(mdata))
        return redirect(url_for('index'))    
    return render_template('index.html',posts1=mdata,posts2=temp,len=n,l=len(temp),ns=4)




@app.route('/',methods=['POST','GET'])
def index():
    session.pop("user",None)
    return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)

login_flag = None
@app.route('/login', methods=['POST',"GET"])
def login():
    
    if request.method == "POST":
        session.pop('user',None)
        email = request.form.get('email')
        passwo = request.form.get('password')
        if email=='':
            return render_template("login.html")
        try:
            cur.execute("select email from public.user Where email = '" + email +"'")
            db_userdata = cur.fetchone()
            userdata=""
            if db_userdata:
                userdata = db_userdata[0]
            if userdata=='':
                return render_template("login.html")

            cur.execute("select passw from public.user Where email = '" + email +"'")
            db_passw = cur.fetchone()
            passw=""
            if db_passw:
                passw = db_passw[0]
        
        except psycopg2.Error as e:
            t_message = e
            return render_template("login.html", message = t_message)
        if email is None:
            flash("no username","danger")
            return render_template("login.html")
        else:
            if sha256_crypt.verify(passwo,passw):
                flash("you are logged in")
                global login_flag
                login_flag=int(0)
                session['user']=email
                d = get_details(email)

                return redirect(url_for('user'))
            else:
                flash("incorrect password","danger")
                return render_template("login.html")

    return render_template('login.html')

@app.route('/signup', methods=['POST',"GET"])
def signup():

    if request.method == "POST":
        if request.form.get('email') =='':
            flash('please fill all details!!!')
            return render_template("signup.html")
        else:    
            firstname = request.form.get('First_Name')
            lastname = request.form.get('Last_Name')
            phone = request.form.get('phone')
            Gender = request.form.get('gender')
            Genre = request.form.get('genre')
            email = request.form.get('email')
            passw = request.form.get('password')
            passw2 = request.form.get('password2')

            if firstname=='' or lastname =='' or passw=='' or passw2=='':
                flash('please fill all details!!!')
                return render_template("signup.html")

            
            t = email_validation(email)
            if t == 0:
                if passw == passw2:
                    securepassw = sha256_crypt.encrypt(str(passw))
                    try:
                        cur.execute("INSERT INTO public.user (firstname,lastname,phone,gender,genre,email,passw) VALUES (%s,%s,%s::bigint,%s,%s,%s,%s)",(firstname,lastname,phone,Gender,Genre,email,securepassw));
                        con.commit()
                    except:
                        flash("wrong data entered")
                        return render_template("signup.html")
                    return redirect(url_for('login'))
                else:
                    flash("incorrect password","danger")
                    return render_template("signup.html")
            else:
                flash('user already exist')
                return redirect(url_for('login'))
    return render_template('signup.html')


def email_validation(em):
    cur.execute("select * from public.user;")
    rows = cur.fetchall()
    for row in rows:
        if em == row[6]:
            return 1
    return 0
        

@app.route('/changeuser1',methods=['POST',"GET"])
def change_userdet():
    if request.method == "POST":
        if request.form.get('password') =='':
            return redirect(url_for('user'))
        else: 
            det=get_details(session['user'])
            firstname = request.form.get('firstname')
            if firstname=='':
                firstname=det[1]
            lastname = request.form.get('lastname')
            if lastname=='':
                lastname=det[2]
            phone = request.form.get('phone')
            if phone=='':
                phone=det[3]
            Gender = request.form.get('Gender')
            if Gender=='':
                Gender=det[4]
            Genre = request.form.get('genre')
            if Genre=='':
                Genre=det[5]
            passw = request.form.get('password')

            if passw=='':
                passw=det[7]
            else:
                passw=sha256_crypt.encrypt(str(passw))

            print("\nuser ",det,firstname,lastname,phone,Gender,Genre)
            
            cur.execute( " update  public.user set firstname = '" + firstname + "', lastname = '" + lastname + "', phone = " + phone + ", gender = '" + Gender + "', genre ='" +Genre + "', passw = '" + passw + "' Where email = '" + session['user'] +"'")
            con.commit()
            return redirect(url_for('user'))
    return redirect(url_for('user'))


    
@app.route('/changeuser',methods=['POST',"GET"])    
def change():
    # return redirect(url_for('change1'))
    return render_template('changeuser.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/movielink',methods=['POST','GET'])
def movielink():
    displaypic=request.form.get('displaypic')
    name=request.form.get('name')
    year=request.form.get('year')
    rating=request.form.get('rating')
    genre=request.form.get('genre')
    print(displaypic,"\n",name,"\n",year,"\n",rating,"\n",genre,"\n")
    lst.clear()
    lst.append(displaypic)
    lst.append(name)
    lst.append(year)
    lst.append(rating)
    lst.append(genre)
    return redirect(url_for('stream'))

@app.route('/movie')
def stream():
    print("stream_site")
    movie_name = lst[1]
    movie_name = movie_name.strip()
    mlink = stream_link(movie_name)
    msummary=movie_summary(movie_name.strip())
    return render_template('movielink.html',displaypic=lst[0],name=lst[1],year=lst[2],rating=lst[3],genre=lst[4],summary=msummary,mstream=mlink)

recommended_movies=None
@app.route('/user')
def user():
    if g.user:
        det=get_details(session['user'])
        global login_flag
        if login_flag==0:
            try:
                cur.execute("select * from public.usermovie Where email = '" + session['user'] +"'");
                usermoviedata = cur.fetchall()
            except:
                print("error in recommendation")
                #new user
            closest_u=closest(usermoviedata)
            global recommended_movies
            recommended = recommend(closest_u)
            recommended_movies=movie_name(recommended)
            login_flag=int(1)
            ### colaborative model (pass userid and movie id format from code ...) 
        print(recommended_movies)
        if recommended_movies==None:
            return redirect(url_for('index'))
        return render_template('user.html',user=session['user'],rdata=recommended_movies,det=det,posts1=mdata,posts2=temp,len=n,ns=4,len1=len(recommended_movies))
    return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)

import pandas as pd
def movie_name(data):
    df=pd.read_csv("closest_users.csv")
    df2=pd.read_csv("movie_image2.csv")
    name_lst=[]
    for i in data:
        t=df.Movieid2[df.Movieid1 == i[0]].values
        if len(t)>1:
            x=t[0]
        try:
            temp = df2[df2.index==x].values.tolist()
            name_lst.append([temp[0][0],temp[0][1],temp[0][2],temp[0][3],temp[0][4],temp[0][5]])
        except:
            print(" movie not found ")

    return name_lst

def update_db(d,a):
    cur.execute("select * from public.user Where email = '" + session['user'] +"'")
    row = cur.fetchone()
    lst=row[5].split(',')
    temp = 1
    for i in lst:
        if i == a:
            temp = 0
            break
    if temp ==1:
        lst.append(a)
        st=','.join(lst)
        cur.execute( " update  public.user set  genre ='" + st + "' Where email = '" + session['user'] +"'")
        con.commit()

def update_M_db(mname, email, uid, rating):
    temp_lst=[]
    for i in movie_name_lst:
        temp_lst.append(i[1])
    t = difflib.get_close_matches(mname,temp_lst)
    for i in t:
        mlistindex = temp_lst.index(i)
        movie_id = movie_name_lst[mlistindex][0]
        try:
            cur.execute("INSERT INTO public.usermovie (email,userid,movieid,rating) VALUES (%s,%s::bigint,%s::bigint,%s::bigint)",(email,uid,movie_id,rating));
            con.commit()
        except:
            print("cannot enter data")        

@app.route('/textanalysis',methods=['POST',"GET"])
def text_analysis():
    if request.method == "POST":
        if request.form.get('genrename') =='':
            return redirect(url_for('user'))
        else:
            print("input") 
            det=get_details(session['user'])
            moviename = request.form.get('moviename')
            genrename = request.form.get('genrename')
            comment = request.form.get('comment')
            rating = request.form.get('rating')
            label = returnlabel(comment)
            update_M_db(moviename, det[6], det[0], rating)
            if label==1:
                update_db(det,genrename)
            return redirect(url_for('user'))

    return redirect(url_for('user'))


# def update_user_movie():
#     cur.execute("select * from public.user")
#     cur.execute("INSERT INTO public.user (firstname,lastname,phone,gender,genre,email,passw) VALUES (%s,%s,%s::bigint,%s,%s,%s,%s)",(firstname,lastname,phone,Gender,Genre,email,passw));


def get_details(sess):
    cur.execute("select * from public.user")
    rows = cur.fetchall()
    for row in rows:
        # print ("ID = ", row[0])
        # print ("firstNAME = ", row[1])
        # print ("lastNAME = ", row[2])
        # print ("phone = ", type(row[3]))
        # print ("gender = ", row[4])
        # t=row[5].split(',')
        # t.append('emotional')
        # print ("genre = ",row[5])
        # print ("email = ", row[6])
        # print ("password = ", row[7], "\n")
        # print(sess)
        if sess == row[6]:
            print(row)
            return row


@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user=session['user']

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for('user'))

@app.route('/contactus',methods=['POST',"GET"])
def send_email():
    if request.method == "POST":
        if request.form.get('email') =='':
            return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
        else:
            print("input") 
            email = request.form.get('email')
            phone = request.form.get('phone')
            subject = request.form.get('subject')
            message = request.form.get('message')

            cur.execute("INSERT INTO public.usermessage (email,phone,subject,message) VALUES (%s,%s::bigint,%s,%s)",(email,phone,subject,message));
            con.commit()
            return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)

@app.route('/contactus1',methods=['POST',"GET"])
def send_email1():
    if request.method == "POST":
        if request.form.get('email') =='':
            return redirect(url_for('user'))
        else:
            print("input") 
            email = request.form.get('email')
            phone = request.form.get('phone')
            subject = request.form.get('subject')
            message = request.form.get('message')
            cur.execute("INSERT INTO public.usermessage (email,phone,subject,message) VALUES (%s,%s::bigint,%s,%s)",(email,phone,subject,message));
            con.commit()
            return redirect(url_for('user'))
    return redirect(url_for('user'))

###########################################################################

app.secret_key="jzdbvkjbhjvhjzfshfzhjfbzhxbfhzb"
app.run(debug=True)

