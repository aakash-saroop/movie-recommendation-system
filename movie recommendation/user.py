from flask import Flask,render_template,request,flash,session,url_for,g,redirect
import imdb
from movie import webscrap
from passlib.hash import sha256_crypt
import psycopg2
from math import ceil

app=Flask(__name__)

con = psycopg2.connect(
    host = "127.0.0.1",
    database = "movierecommender",
    user = "postgres",
    password = "admin",
    port="5432")

cur=con.cursor()

class User:
    def __init__(self,id,email,password):
        self.id=id
        self.email=email
        self.password=password

    def __repr__(self):
        return f'<User: {self.id}>'

top = webscrap()
a={"admin@gmail.com":"qwerty"}
ia1=imdb.IMDb()

@app.route('/')
def index():
    print(type(top[0]))
    session.pop("user",None)
    n=len(top)
    print(type(n))
    nslides= n//4 +ceil((n/4)-(n//4))
    print(type(nslides))
    if nslides>8:
        nslides=int(8)
    return render_template('index.html',posts=top,ia=ia1,len=n,ns=nslides)
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
            userdata = cur.fetchone()[0]

            cur.execute("select passw from public.user Where email = '" + email +"'")
            passw = cur.fetchone()[0]
        
        except psycopg2.Error as e:
            t_message = e
            print(e," dsbsjd")
            return render_template("login.html", message = t_message)
        print("hello")
        if email is None:
            flash("no username","danger")
            return render_template("login.html")
        else:
            if passw == passwo:
                flash("you are logged in")
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
            Genre = list(request.form.get('genre').split(','))
            email = request.form.get('email')
            passw = request.form.get('password')
            passw2 = request.form.get('password2')
            securepassw = sha256_crypt.encrypt(str(passw))
            if passw == passw2:
                cur.execute("INSERT INTO public.user (firstname,lastname,phone,gender,genre,email,passw) VALUES (%s,%s,%s::bigint,%s,%s,%s,%s)",(firstname,lastname,phone,Gender,Genre,email,passw));
                con.commit()
                con.close()
                return render_template("login.html")
            else:
                flash("incorrect password","danger")
                return render_template("signup.html")


    return render_template('signup.html')

# @app.route('/changeuser',methods=['POST',"GET"])
# def change():
#     if request.method == "POST":
#         if request.form.get('genre') =='':
#             return redirect(url_for('user'))
#         else: 
#             det=get_details(session['user'])
#             firstname = request.form.get('First_Name')
#             lastname = request.form.get('Last_Name')
#             phone = request.form.get('phone')
#             Gender = request.form.get('gender')
#             Genre = list(request.form.get('genre').split(','))

#             return redirect(url_for('user'))

#     return redirect(url_for('user'))
    
@app.route('/changeuser')    
def change():
    return render_template('changeuser.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')


@app.route('/user')
def user():
    if g.user:
        #     user = session['user']
        #     return f"<h1>{user}</h1>"
        # else:
        #             return redirect(url_for('login'))
        det=get_details(session['user'])
        return render_template('user.html',user=session['user'],det=det)
    return render_template('index.html',posts=top,ia=ia1)
    
def get_details(sess):
    cur.execute("select * from public.user")
    rows = cur.fetchall()
    for row in rows:
        print ("ID = ", row[0])
        print ("firstNAME = ", row[1])
        print ("lastNAME = ", row[2])
        print ("phone = ", row[3])
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




@app.route("/logout")
def logout():
    session.pop("user",None)
    return render_template('index.html',posts=top,ia=ia1)

@app.before_request
def before_request():
    g.user=None
    
    if 'user' in session:
        g.user=session['user']




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


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    for i in a:
        if i ==email:
            if password == a[i]:
                return render_template('user.html')

    return "email is {} and password is ".format(email,password)


app.secret_key="jzdbvkjbhjvhjzfshfzhjfbzhxbfhzb"
app.run(debug=True)
    

