from flask import Flask, render_template, request, redirect, url_for, session
import secrets

secret_key = secrets.token_hex(16)



users =[{
    "name": "roni", 
    "password": "1234", 
    "color": "#206A5D"
    }]

colors = ["#206A5D", "#81B214", "#FFCC29", "#F58634"]

app = Flask(__name__)

app.secret_key = secret_key

def checkUser(username, password):
    for name in users:
        if name["name"] == username:
            if name["password"] == password:
                return True 
            else: return False
    else: return False 



@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/log-in", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        print(name, password)
        if checkUser(username=name, password=password):
            session['username'] = name
            session['profile'] = name[0]
            return redirect(url_for("home"))
        else: return "Invalid credentials", 401 
    return render_template("login.html")

@app.route("/sign-in",  methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password-2")
        # color = request.form.get("")
        if password == password2:
            new_user = {"name": name, "password": password}
            users.append(new_user)
            print(users)
            return redirect(url_for('home'))
        else: 
            return render_template('sign.html', password2_error=True)
      
    return render_template('sign.html')

@app.route("/home")
def home():
    if 'username' in session:
        username = session["username"]
        profile = session['profile']
        if profile.isalpha():
            profile = profile.upper()
        return render_template("home.html", username = username, profile = profile)
    else: 
        return redirect(url_for("login"))

  




if __name__ == "__main__":
    app.run(debug = True, port = 8080)