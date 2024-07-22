from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import secrets
from users import users
from datetime import datetime

secret_key = secrets.token_hex(16)

colors = ["#206A5D", "#81B214", "#FFCC29", "#F58634"]

weight_input = []
meals_list = []
water_list = []
workout_list =[]
favorite_meals = []


app = Flask(__name__)

app.secret_key = secret_key

def checkUser(username, password):
    for name in users:
        if name["name"] == username:
            if name["password"] == password:
                return True 
            else: return False
    else: return False 

def get_user_color(username):
    for user in users:
        if user["name"] == username:
            return user["color"]
    return None 

def get_user_fav_meals(username):
    for user in users:
        if user["name"] == username:
            return user["fav_meals"]
    return [{"no fav meals yet": "true"}]

def get_user_water(username):
     for user in users:
          if user["name"] == username:
               return user["water"]
     return []

def get_user_weight(username):
    for user in users:
          if user["name"] == username:
               return user["weight"]
    return []

def get_user_meals(username):
    for user in users:
          if user["name"] == username:
               return user["meals"]
    return []

def get_user_workout(username):
    for user in users:
          if user["name"] == username:
               return user["workout"]
    return []


@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/log-in", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        # print(name, password)
        if checkUser(username=name, password=password):
            session['username'] = name
            session['profile'] = name[0]
            session["color"] = get_user_color(name)
            session["fav_meals"] = get_user_fav_meals(name)
            session["water"] = get_user_water(name)
            session["weight"] = get_user_weight(name)
            session["meals"] = get_user_meals(name)
            session["workout"] = get_user_workout(name)
            session["fav_meal"] = get_user_fav_meals(name)
            return redirect(url_for("home"))
        else: return "Invalid credentials", 401 
    return render_template("login.html")

@app.route("/sign-in",  methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password-2")
        color = request.form.get("color")
        # print(color)
        if password == password2 and color:
            new_user = {"name": name, "password": password, "color": color,
                            "water": [],
                            "weight": [],
                            "meals": [],
                            "workout": [],
                            "fav_meals" :[{"no fav meals yet": "true"}] }
            session['username'] = name
            session['profile'] = name[0]
            session["color"] = color
            session["fav_meals"] = new_user["fav_meals"]
            session["water"] = new_user["water"]
            session["weight"] = new_user["weight"]
            session["meals"] = new_user["meals"]
            session["workout"] = new_user["workout"]
            users.append(new_user)
            # print(users)
            return redirect(url_for('home'))
        else: 
            return render_template('sign.html', password2_error=True)
      
    return render_template('sign.html')

@app.route("/home")
def home():
    if 'username' in session:
        username = session["username"]
        profile = session['profile']
        color = session['color']
        favorite_meals = session['fav_meals']
        if profile.isalpha():
            profile = profile.upper()
        return render_template("home.html", username = username, 
                               profile = profile, 
                               color = color, 
                               meals = favorite_meals)
    else: 
        return redirect(url_for("login"))

  
@app.route("/weight", methods = ["POST"])
def weight():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        weight_unit = data.get('weight')
        measurement = data.get('measurement')
        date = data.get('date')
        response_data = {
            "weight_unit" : measurement,
            "weight_num": weight_unit,
            "date": date
        }
        weight_input.append(response_data)
        session["weight"] = weight_input
        print(session["weight"] )

        return jsonify(response_data)

@app.route("/meals", methods = ["POST"])
def meals():
        data = request.get_json()
        if data:
            meal = data.get('meal')
            time = data.get('time')
            date = data.get("date")
            response_data = {
                "meal" : meal,
                "time": time,
                "date" : date
            }
            session['meals'].append(response_data)
            print(meals_list)
            return jsonify(response_data)

@app.route("/water", methods = ["POST"])
def water():
        data = request.get_json()
        water_quantity = data.get('quantity')
        time = data.get('time')
        date = data.get('date')
        response_data = {
            "water-form" : water_quantity,
            "time": time,
            "date" : date
        }
        water_list.append(response_data)
        print(water_list)
        return jsonify(response_data)

@app.route("/workout", methods = ["POST"])
def workout():
        data = request.get_json()
        workout_type = data.get('workout_type')
        time = data.get('time')
        date = data.get('date')
        response_data = {
            "wokout-type" : workout_type,
            "time": time,
            "date" : date
        }
        workout_list.append(response_data)
        print(workout_list)
        return jsonify(response_data)


@app.route("/add_meal")
def add_meal():
        if 'username' in session:
            username = session["username"]
            profile = session['profile']
            color = session['color']
            favorite_meals = session['fav_meal']
            if profile.isalpha():
                profile = profile.upper()
            return  render_template("add_meal.html", username = username,
                                     profile = profile, 
                                     color = color, 
                                     meals = favorite_meals)
        else: 
            return redirect(url_for("login"))
        
@app.route("/meal_edited", methods=["POST"])
def meal_edited():
        data = request.get_json()
        session["fav_meals"] = data
        print( favorite_meals)
        response_data = {
             "massage": "Favorite meals updated successfully",
             "data": favorite_meals
        }
        return jsonify(response_data)
 
@app.route("/logout")
def logout():
     session.pop("username", None)
     session.pop('profile', None)
     session.pop("color", None)
     session.pop("fav_meals", None)
     session.pop("water", None)
     session.pop("weight", None)
     session.pop("workout", None)
     return redirect(url_for("login"))

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if 'username' in session:
        username = session["username"]
        profile = session['profile']
        color = session['color']
        favorite_meals = session["fav_meals"]
        weight = session['weight']
        water = session['water']
        workout = session['workout']
        meals = session['meals']
        if profile.isalpha():
            profile = profile.upper()
        return render_template("profile.html", username = username, 
                               profile = profile, 
                               color = color, 
                               fav_meals = favorite_meals,
                               date = datetime.today().strftime('%Y-%m-%d'),
                               weight =weight,
                               water = water,
                               workout = workout,
                               meals = meals
                               )
    else: 
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug = True, port = 8080)