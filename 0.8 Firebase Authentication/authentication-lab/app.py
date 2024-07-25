from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config={
  "apiKey": "AIzaSyCI2-w19VwMNJ23WaoJHgjVGWvsfs5v-K8",
  "authDomain": "labdiaa.firebaseapp.com",
  "projectId": "labdiaa",
  "storageBucket": "labdiaa.appspot.com",
  "messagingSenderId": "18038657292",
  "appId": "1:18038657292:web:650426de8d59e3e623f929",
  "measurementId": "G-Z0S090V010",
  "databaseURL": "https://labdiaa-default-rtdb.europe-west1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db=firebase.database()
start=0


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('menu'))

        except:
           error = "Authentication failed"
    return render_template("signin.html")

@app.route('/menu',methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return render_template("menu.html")

@app.route('/easy', methods=['GET', 'POST'])
def easy():
    if request.method == 'GET':

        return render_template("easy.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('menu'))
        except Exception as e:
           print(e)
           error = "Authentication failed"
        return redirect(url_for('menu'))

    else:
        return render_template("signup.html")

@app.route('/medium', methods=['GET', 'POST'])
def medium():
    if request.method == 'GET':
        return render_template("medium.html")

@app.route('/hard', methods=['GET', 'POST'])
def hard():
    if request.method == 'GET':
        return render_template("hard.html")


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template("thanks.html")

@app.route('/submit', methods=['GET','POST'])
def submit():
    db.child('users').child(login_session['user']['localId']).set({"score":100})
    UID=login_session['user']['localId']
    user=db.child("users").child(UID).get().val()
    return render_template(".html")

if __name__ == '__main__':
    app.run(debug=True)