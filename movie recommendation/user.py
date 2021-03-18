from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/changeuser')
def change():
    return render_template('changeuser.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/user')
def user():
    return render_template('user.html')
app.run(debug=True)
