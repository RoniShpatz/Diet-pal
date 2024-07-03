from flask import Flask, render_template, request, redirect, url_for




app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/sign-in")
def sign_in():
    return render_template("sign.html")






if __name__ == "__main__":
    app.run(debug = True, port = 8080)