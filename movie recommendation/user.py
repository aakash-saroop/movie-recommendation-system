from flask import Flask,render_template,request,flash,session,url_for,g,redirect,jsonify
import imdb
from movie import webscrap
from passlib.hash import sha256_crypt
import psycopg2
from math import ceil
from textanalysis import returnlabel
import smtplib
from flask_mail import Mail
import json
import re
from stream_sites import stream_link

app=Flask(__name__)

con = psycopg2.connect(
    host = "127.0.0.1",
    database = "movierecommender",
    user = "postgres",
    password = "admin",
    port="5432")

cur=con.cursor()
cur.execute("select * from public.moviedatabase")
mdata = cur.fetchall()
n=len(mdata)
temp=mdata.copy()
nslides= n//4 +ceil((n/4)-(n//4))

# top = webscrap()
a={"admin@gmail.com":"qwerty"}
# ia1=imdb.IMDb()
lst=[]

@app.route('/filter',methods=['POST','GET'])
def filter():
    
    if request.get_data().decode('utf-8').strip()=="Action":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Action", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))
        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Comedy":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Comedy", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        # return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Drama":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Drama", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Horror":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Horror", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Romance":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Romance", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        # return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata,l=len(temp)),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Documentry":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Documentry", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Animation":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Animation", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    else :
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            temp.append(mpdata[i])
            count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,l=len(temp),len=n,ns=4)
    
    return render_template('index.html',posts1=mdata,posts2=temp,len=n,l=len(temp),ns=4)



@app.route('/filter2',methods=['POST','GET'])
def filter2():
    
    if request.get_data().decode('utf-8').strip()=="Action":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Action", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))
        return redirect(url_for('user'))
    elif request.get_data().decode('utf-8').strip()=="Comedy":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Comedy", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        # return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Drama":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Drama", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Horror":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Horror", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Romance":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Romance", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        # return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata,l=len(temp)),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Documentry":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Documentry", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    elif request.get_data().decode('utf-8').strip()=="Animation":
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            txt = mpdata[i][4]
            x = re.findall("Animation", txt)
            if len(x)!=0:
                temp.append(mpdata[i])
                count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)
    else :
        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))

        print("///////////////////////////////////////////////////////")
        print("*************************",request.get_data().decode('utf-8'))
        print(type(temp))
        mpdata=mdata.copy()
        temp.clear() 
        count=0
        for i in range(n):
            temp.append(mpdata[i])
            count+=1      

        print(len(temp),len(mdata))

        return redirect(url_for('index'))

        return render_template('index.html',posts1=mdata,posts2=temp,l=len(temp),len=n,ns=4)
    
    return render_template('index.html',posts1=mdata,posts2=temp,len=n,l=len(temp),ns=4)




@app.route('/',methods=['POST','GET'])
def index():
    session.pop("user",None)
    # print(json.dumps(request.form['data']))
    print(len(mdata))
    
    # print(type(nslides))
    return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)

    
@app.route('/login', methods=['POST',"GET"])
def login():
    
    if request.method == "POST":
        session.pop('user',None)
        email = request.form.get('email')
        passwo = request.form.get('password')
        if email=='':
            return render_template("login.html")
        print("email ",email,"pass ",passwo)
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
            print(e," dsbsjd")
            return render_template("login.html", message = t_message)
        print("hello")
        if email is None:
            flash("no username","danger")
            print("email")
            return render_template("login.html")
        else:
            if passw == passwo:
                flash("you are logged in")
                print(email)
                session['user']=email
                d = get_details(email)
                print(type(d))

                return redirect(url_for('user'))
                # return render_template("user.html")
                # return redirect(url_for('user'))
            else:
                flash("incorrect password","danger")
                return render_template("login.html",posts=top,ia=ia1)

    return render_template('login.html')

@app.route('/signup', methods=['POST',"GET"])
def signup():

    if request.method == "POST":
        if request.form.get('email') =='':
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
            securepassw = sha256_crypt.encrypt(str(passw))
            print(email,type(email))
            t = email_validation(email)
            print("t=====",t)
            if t == 0:
                if passw == passw2:
                    cur.execute("INSERT INTO public.user (firstname,lastname,phone,gender,genre,email,passw) VALUES (%s,%s,%s::bigint,%s,%s,%s,%s)",(firstname,lastname,phone,Gender,Genre,email,passw));
                    con.commit()
                    return redirect(url_for('login'))
                else:
                    flash("incorrect password","danger")
                    return render_template("signup.html")
            else:
                return redirect(url_for('login'))
    return render_template('signup.html')


def email_validation(em):
    cur.execute("select * from public.user;")
    rows = cur.fetchall()
    print("in email")
    for row in rows:
        print ("email = ", row[6])
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

            print("\nahsdnisu ",det,firstname,lastname,phone,Gender,Genre)
            
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
    print(displaypic,"\n",name,"\n",year,"\n",rating,"\n",genre,"\n","hello")
    lst.clear()
    lst.append(displaypic)
    lst.append(name)
    lst.append(year)
    lst.append(rating)
    lst.append(genre)
    return redirect(url_for('stream'))
    return render_template('movielink.html',displaypic=displaypic,name=name,year=year,rating=rating,genre=genre)

@app.route('/movie')
def stream():
    print("dfgfgfggd")
    movie_name = lst[1]
    movie_name = movie_name.strip()
    mlink = stream_link(movie_name)
    return render_template('movielink.html',displaypic=lst[0],name=lst[1],year=lst[2],rating=lst[3],genre=lst[4],mstream=mlink)

@app.route('/user')
def user():
    if g.user:
        det=get_details(session['user'])
        ### colaborative model (pass userid and movie id format from code ...) 
        return render_template('user.html',user=session['user'],det=det,posts1=mdata,posts2=temp,len=n,ns=4)
    return render_template('index.html',posts1=mdata,posts2=temp,len=len(mdata),l=len(temp),ns=4)

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

@app.route('/textanalysis',methods=['POST',"GET"])
def text_analysis():
    if request.method == "POST":
        print("in")
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
            if label==1:
                update_db(det,genrename)

            return redirect(url_for('user'))

    return redirect(url_for('user'))

def get_details(sess):
    cur.execute("select * from public.user")
    rows = cur.fetchall()
    for row in rows:
        print ("ID = ", row[0])
        print ("firstNAME = ", row[1])
        print ("lastNAME = ", row[2])
        print ("phone = ", type(row[3]))
        print ("gender = ", row[4])
        t=row[5].split(',')
        t.append('emotional')
        print ("genre = ",row[5])
        print ("email = ", row[6])
        print ("password = ", row[7], "\n")
        print(sess)
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
        print("in")
        if request.form.get('email') =='':
            return render_template('index.html',posts=mdata,len=n,ns=4)
        else:
            print("input") 
            email = request.form.get('email')
            phone = request.form.get('phone')
            subject = request.form.get('subject')
            message = request.form.get('message')
            cur.execute("INSERT INTO public.usermessage (email,phone,subject,message) VALUES (%s,%s::bigint,%s,%s)",(email,phone,subject,message));
            con.commit()
            return render_template('index.html',posts=mdata,len=n,ns=4)
    return render_template('index.html',posts=mdata,len=n,ns=4)

@app.route('/contactus1',methods=['POST',"GET"])
def send_email1():
    if request.method == "POST":
        print("in")
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
            print("done")
            return redirect(url_for('user'))
    return redirect(url_for('user'))

###########################################################################


@app.route('/registeruser', methods=['POST'])

def registeruser():
    firstname = request.form.get('First_Name')
    lastname = request.form.get('Last_Name')
    phone = request.form.get('phone')
    Gender = request.form.get('gender')
    Genre = list(request.form.get('genre').split(','))
    email = request.form.get('email')
    passw = request.form.get('password')
    return "email is {} and password is {} {} {} {} {} {}".format(Genre,Gender,firstname,passw,lastname,phone)





app.secret_key="jzdbvkjbhjvhjzfshfzhjfbzhxbfhzb"
app.run(debug=True)
    

'''
if ($i==1)
    	{console.log("Action");
		qurl='http://127.0.0.1:5000/'
	$.ajax({
            type: "POST",
            cache: false,
            data:"Action",
            url: qurl,
            dataType: "json",
            success: function(data) { 
                console.log(data);                    
            },
            error: function(jqXHR) {
                alert("error: " + jqXHR.status);
                console.log(jqXHR);
            }
        })
'''