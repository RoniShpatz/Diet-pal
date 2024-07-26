from flask import Flask, render_template, request, redirect, url_for, session, jsonify


from datetime import datetime, timedelta
import json

secret_key = "my_secret_key"

colors = ["#206A5D", "#81B214", "#FFCC29", "#F58634"]

weight_input = []
meals_list = []
water_list = []
workout_list =[]
favorite_meals = []

# declaring users from json file to get permanent and  persistence
with open("users_data.json" , 'r') as f:
        users = json.load(f)

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
        if user['name'] == username:
            return user["fav_meals"]
    return None

def get_user_meals(username):
    for user in users:
        if user['name'] == username:
            return user["meals"]
    return None

def get_user_water(username):
    for user in users:
        if user['name'] == username:
            return user["water"]
    return None

def get_user_weight(username):
    for user in users:
        if user['name'] == username:
            return user["weight"]
    return None

def get_user_workout(username):
    for user in users:
        if user['name'] == username:
            return user["workout"]
    return None

def check_user_name(username):
    for user in users:
        if user['name'] == username:
            return True
        else: return False

def update_user_lists(username):
    for user in users:
        if user['name'] == username:
            user['water'] = water_list
            user['weight'] = weight_input
            user['meals'] = meals_list
            user['workout'] = workout_list

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
            global favorite_meals
            favorite_meals = get_user_fav_meals(name)
            global meals_list
            global weight_input
            global water_list
            global workout_list
            meals_list = get_user_meals(name)
            water_list = get_user_water(name)
            meals_list = get_user_meals(name)
            workout_list = get_user_workout(name)
            weight_input = get_user_weight(name)
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
        isUniq = check_user_name(name)
        # print(color)
        if password == password2 and color and isUniq == False :
            new_user = {"name": name, "password": password, "color": color,
                            "water": [],
                            "weight": [],
                            "meals": [],
                            "workout": [],
                            "fav_meals" :[{"no fav meals yet": "true"}] }
            session['username'] = name
            session['profile'] = name[0]
            session["color"] = color
            users.append(new_user)
            # print(users)
            return redirect(url_for('home'))
        else:
            if password != password2:
                return render_template('sign.html', password2_error=True, name= False)
            else: return render_template('sign.html', password2_error=False, name= True)
           
      
    return render_template('sign.html')

@app.route("/home")
def home():
    if 'username' in session:
        username = session["username"]
        profile = session['profile']
        color = session['color']
        global favorite_meals
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
    
        print(weight_input )

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
            meals_list.append(response_data)
            print(meals_list)
            return jsonify(response_data)

@app.route("/water", methods = ["POST"])
def water():
        data = request.get_json()
        water_quantity = data.get('quantity')
        time = data.get('time')
        date = data.get('date')
        response_data = {
            "quantity": int(water_quantity),
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
        duration = data.get('duration')
        date = data.get('date')
        response_data = {
            "type" : workout_type,
            "duration": duration,
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
            global favorite_meals
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
        global favorite_meals
        favorite_meals = data
        print( favorite_meals)
        response_data = {
             "massage": "Favorite meals updated successfully",
             "data": favorite_meals
        }
        return jsonify(response_data)



def format_date(date):
    return date.strftime('%d/ %m/ %Y')

def day_before(date_str):
    return (datetime.strptime(date_str, '%d/ %m/ %Y') - timedelta(days=1)).strftime('%d/ %m/ %Y')

def day_after(date_str):
    return (datetime.strptime(date_str, '%d/ %m/ %Y') + timedelta(days=1)).strftime('%d/ %m/ %Y')

current_day = ""

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if 'username' in session:
        username = session["username"]
        profile = session['profile']
        color = session['color']
        global favorite_meals
        global weight_input
        global water_list
        global workout_list
        global meals_list
        global is_date_set
        if 'day_today' not in session:
            session['day_today'] = datetime.today().strftime('%d/ %m/ %Y')

        date_today = session['day_today']
        print(date_today)
        if profile.isalpha():
            profile = profile.upper()
        return render_template("profile.html", username = username, 
                               profile = profile, 
                               color = color, 
                               fav_meals = favorite_meals,
                               date = date_today,
                               weight =weight_input,
                               water =  water_list,
                               workout = workout_list,
                               meals = meals_list
                               )
    else: 
        return redirect(url_for("login"))


@app.route("/next", methods=["POST"])
def next():
    if 'username' in session:
        print(session['day_today'])
        session['day_today'] = day_after(session['day_today'])
        print(session['day_today'])
        return redirect (url_for('profile'))
    else: return redirect(url_for('login'))
      
        
@app.route("/prev", methods=["POST"])
def prev():
    if 'username' in session:
        if 'day_today' in session:
            session['day_today'] = day_before(session['day_today'])
            print(session['day_today'])
        return redirect (url_for('profile'))
    else: 
        return redirect(url_for("login")) 
    
 
@app.route("/delet_weight/<int:weight_id>", methods=["POST", "GET"])
def delete_weight(weight_id):
    if 'username' in session:
        action = request.form.get('action', None)
        print(action)
        if action == 'Submit':
            weight_num = request.form.get('weight_num', None)
            print(weight_num)
            if weight_num:
                if 0 <= weight_id < len(weight_input):
                    weight_to_change = weight_input[weight_id]
                    weight_to_change['weight_num'] = weight_num
                    print(weight_input)
                else:
                    raise IndexError("Invalid weight_id")         
        elif action == "Reset":
            if 0 <= weight_id < len(weight_input):
                weight_input.pop(weight_id)
            else: IndexError("Invalid weight_id")
        return redirect(url_for("profile"))
    else: 
        return redirect(url_for("login")) 

@app.route("/delet_meal/<int:meal_id>", methods=["POST", "GET"])
def delete_meal(meal_id):
    if 'username' in session:
        action = request.form.get('action', None)
        # print(action)
        if action == 'Submit':
            meal_time = request.form.get('meal_time', None)
            meal_content = request.form.get('meal_content', None)
            if meal_time and meal_content:
                if 0 <= meal_id < len(meals_list):
                    meal_to_change = meals_list[meal_id]
                    meal_to_change['meal'] = meal_content
                    meal_to_change['time'] = meal_time
                    # print(meals_list)
                else:
                    raise IndexError("Invalid weight_id")         
        elif action == "Reset":
            if 0 <= meal_id < len(meals_list):
                meals_list.pop(meal_id)
            else: IndexError("Invalid meal_id")
        return redirect(url_for("profile"))
    else: 
        return redirect(url_for("login")) 

@app.route("/add_water", methods=["POST", "GET"])
def add_water():
    if 'username' in session:
        water_new_value = request.form.get('water_num', None)
        new_date_value = session["day_today"]
        new_time_value = datetime.now().strftime('%H:%M')
        water_list.append({"quantity": int(water_new_value), "time":new_time_value, "date": new_date_value})
        return redirect(url_for("profile"))
    else: 
        return redirect(url_for("login")) 

@app.route("/edit_workout/<int:workout_id>", methods=["POST", "GET"])
def edit_workout(workout_id):
    if 'username' in session:
        action = request.form.get('action', None)
        if action == "Submit":
            new_workout = request.form.get('new_workout', None)
            new_time_workout = request.form.get('time_workout', None)
            if new_workout and new_time_workout:
                if 0 <= workout_id <= len(workout_list):
                    workout_to_cahnge = workout_list[workout_id]
                    workout_to_cahnge["type"] = new_workout
                    workout_to_cahnge["duration"] = new_time_workout
                    return redirect(url_for("profile"))
                else:
                    raise IndexError("Invalid workout_id")  
        elif action == "Reset":
            if 0 <= workout_id < len(workout_list):
                workout_list.pop(workout_id)
            else:
                raise IndexError("Invalid workout_id") 
            return redirect(url_for("profile"))
    else: 
        return redirect(url_for("login")) 


@app.route("/logout")
def logout():
  
     username = session["username"]
 
     update_user_lists(username)
     with open('users_data.json', 'w') as f:
          json.dump(users, f)
     session.pop("username", None)
     session.pop('profile', None)
     session.pop("color", None)
     session.pop("day_today", None)
     global weight_input
     weight_input = []
     global meals_list 
     meals_list = []
     global water_list 
     water_list = []
     global workout_list
     workout_list = []
     global favorite_meals
     favorite_meals = []
     return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True, port = 8080)

main = app