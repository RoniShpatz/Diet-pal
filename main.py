from flask import Flask, render_template, request, redirect, url_for, session, jsonify


from datetime import datetime, timedelta
import json

secret_key = "my_secret_key"

colors = ["#206A5D", "#81B214", "#FFCC29", "#F58634"]


app = Flask(__name__)

app.secret_key = secret_key

# reading json file to get permanent and  persistence and using it to update 

def checkUser(username, password):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    for name in users:
        if name["name"] == username:
            if name["password"] == password:
                return True 
            else: return False
    else: return False 

def get_user_color(username):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    for user in users:
        if user["name"] == username:
            return user["color"]
    return None 

def get_user_fav_meals(username):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    for user in users:
        if user['name'] == username:
            return user["fav_meals"]
    return None

def get_user_meals(username):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    for user in users:
        if user['name'] == username:
            return user["meals"]
    return None

def get_user_water(username):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    for user in users:
        if user['name'] == username:
            return user["water"]
    return None

def get_user_weight(username):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    for user in users:
        if user['name'] == username:
            return user["weight"]
    return None

def get_user_workout(username):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    for user in users:
        if user['name'] == username:
            return user["workout"]
    return None

def check_user_name(username):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    for user in users:
        if user['name'] == username:
            return True
        else: return False

def update_user(username, what_to_update, list):
    with open("users_data.json" , 'r') as f:
        users = json.load(f)
    user_found = False
    for user in users:
        if user["name"] == username:
            # print(user["name"])
            user[what_to_update] = list
            with open('users_data.json', 'w') as f:
                json.dump(users, f)
            
            user_found = True
            break
    if not user_found:
        print("no user was found")
       

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
                            "fav_meals" :[] }
            session['username'] = name
            session['profile'] = name[0]
            session["color"] = color
            with open("users_data.json" , 'r') as f:
                users = json.load(f)
            users.append(new_user)
            with open('users_data.json', 'w') as f:
                json.dump(users, f)
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
        favorite_meals = get_user_fav_meals(username)      
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
# Create a local API to send data from the frontend to the backend (JavaScript to Python).
#  This involves preventing the page from refreshing.
    if request.method == 'POST':
        data = request.get_json()
        # print(data)
        weight_unit = data.get('weight')
        measurement = data.get('measurement')
        date = data.get('date')
        response_data = {
            "weight_unit" : measurement,
            "weight_num": weight_unit,
            "date": date
        }
        weight_input = get_user_weight(session["username"])
        for index, item in enumerate(weight_input):
            if item["date"] == response_data["date"]:
                weight_input.pop(index)
                break
        weight_input.append(response_data)
        update_user(session["username"], "weight", weight_input)
        # print(weight_input )
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
            meals_list = get_user_meals(session["username"])
            meals_list.append(response_data)
            update_user(session["username"], "meals", meals_list)
            # print(meals_list)
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
        water_list = get_user_water(session["username"])
        water_list.append(response_data)
        update_user(session["username"], "water", water_list)
        # print(water_list)
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
        workout_list = get_user_workout(session["username"])
        workout_list.append(response_data)
        update_user(session["username"], "workout", workout_list)
        # print(workout_list)
        return jsonify(response_data)


@app.route("/add_meal")
def add_meal():
        if 'username' in session:
            username = session["username"]
            profile = session['profile']
            color = session['color']
            fav_meals = get_user_fav_meals(username)
            if profile.isalpha():
                profile = profile.upper()
            return  render_template("add_meal.html", username = username,
                                     profile = profile, 
                                     color = color, 
                                     meals = fav_meals)
        else: 
            return redirect(url_for("login"))
        
@app.route("/meal_edited", methods=["POST"])
def meal_edited():
        data = request.get_json()
       
        favorite_meals = data
        update_user(session["username"], "fav_meals", favorite_meals)
        response_data = {
             "massage": "Favorite meals updated successfully",
             "data": favorite_meals
        }
        return jsonify(response_data)


# Ensure the date matches between JavaScript and Python, and handle moving 
# forward and background on days correctly
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
        # Getting the data from the JSON file to ensure persistence
        fav_meal = get_user_fav_meals(username)
        meals = get_user_meals(username)
        workout = get_user_workout(username)
        water = get_user_water(username)
        weight = get_user_weight(username)
        if 'day_today' not in session:
            session['day_today'] = datetime.today().strftime('%d/ %m/ %Y')

        date_today = session['day_today']
        # print(date_today)
        if profile.isalpha():
            profile = profile.upper()
        return render_template("profile.html", username = username, 
                               profile = profile, 
                               color = color, 
                               fav_meals = fav_meal,
                               date = date_today,
                               weight = weight,
                               water =  water,
                               workout = workout,
                               meals = meals
                               )
    else: 
        return redirect(url_for("login"))


@app.route("/next", methods=["POST"])
def next():
    if 'username' in session:
        # print(session['day_today'])
        session['day_today'] = day_after(session['day_today'])
        # print(session['day_today'])
        return redirect (url_for('profile'))
    else: return redirect(url_for('login'))
      
        
@app.route("/prev", methods=["POST"])
def prev():
    if 'username' in session:
        if 'day_today' in session:
            session['day_today'] = day_before(session['day_today'])
            # print(session['day_today'])
        return redirect (url_for('profile'))
    else: 
        return redirect(url_for("login")) 
    
#  Getting the data from the JSON file to ensure persistence
@app.route("/delet_weight/<int:weight_id>", methods=["POST", "GET"])
def delete_weight(weight_id):
    if 'username' in session:
        action = request.form.get('action', None)

        # I used the action attribute to recognize which submit button is 
        # clicked—reset to delete the data and submit to change the edited data.
        weight_input = get_user_weight(session['username'])
        if action == 'Submit':
            weight_num = request.form.get('weight_num', None)
            # print(weight_num)
           
            print(weight_input)
            if weight_num:
                if 0 <= weight_id < len(weight_input):
                    weight_to_change = weight_input[weight_id]
                    weight_to_change['weight_num'] = weight_num
                    update_user(session["username"], "weight", weight_input)
                    # print(weight_input)
                else:
                    raise IndexError("Invalid weight_id")   
        elif action == "Reset":
            if 0 <= weight_id < len(weight_input):
                weight_input.pop(weight_id)
                update_user(session["username"], "weight", weight_input)
            else: IndexError("Invalid weight_id")
        return redirect(url_for("profile"))
    else: 
        return redirect(url_for("login")) 

@app.route("/delet_meal/<int:meal_id>", methods=["POST", "GET"])
def delete_meal(meal_id):
    if 'username' in session:
        action = request.form.get('action', None)
        # print(action)
        meals_list = get_user_meals(session['username'])
        if action == 'Submit':
            meal_time = request.form.get('meal_time', None)
            meal_content = request.form.get('meal_content', None)
            if meal_time and meal_content:
                
                if 0 <= meal_id < len(meals_list):
                    meal_to_change = meals_list[meal_id]
                    meal_to_change['meal'] = meal_content
                    meal_to_change['time'] = meal_time
                    update_user(session["username"], "meals", meals_list)
                    
                else:
                    raise IndexError("Invalid weight_id")         
        elif action == "Reset":
            if 0 <= meal_id < len(meals_list):
                meals_list.pop(meal_id)
                update_user(session["username"], "meals", meals_list)
            else: IndexError("Invalid meal_id")
        return redirect(url_for("profile"))
    else: 
        return redirect(url_for("login")) 

@app.route("/add_meal_log", methods=["POST", "GET"])
def add_meal_log():
    if 'username' in session:
        if request.method == "POST":
            time = request.form.get("meal_time")
            content = request.form.get("meal_content")
            meals_list = get_user_meals(session['username'])
            if time and content:
                new_date_value = session["day_today"]
                meals_list.append({"meal": content,
                                   "time": time,
                                   "date": new_date_value})
                update_user(session["username"], "meals", meals_list)
        return redirect(url_for("profile"))
    else:
        return redirect(url_for("login")) 

@app.route("/add_weight_log", methods=["POST", "GET"])
def add_weight_log():
    if 'username' in session:
        if request.method == "POST":
            weight = request.form.get("weight")
            unit = request.form.get("weight_unit")
            date = session["day_today"]
            if weight and unit:
                weight_input = get_user_weight(session['username'])
                new = {"weight_num": weight,
                                     "weight_unit": unit,
                                     "date": date}
                for index, item in enumerate(weight_input):
                    if item["date"] == new["date"]:
                        weight_input.pop(index)
                        break
                weight_input.append(new)

                update_user(session["username"], "weight", weight_input)
        return redirect(url_for("profile"))
    else:
        return redirect(url_for("login")) 

@app.route("/add_workout_log", methods=["POST", "GET"])
def add_workout_log():
    if 'username' in session:
        if request.method == "POST":
            workout= request.form.get("new_workout")
            # print(workout)
            duration = request.form.get("time_workout")
            date = session["day_today"]
            if workout and duration:
                workout_list = get_user_workout(session['username'])
                workout_list.append({"type": workout,
                                     "duration": duration,
                                     "date": date })
                update_user(session["username"], "workout", workout_list)
        return redirect(url_for("profile"))
    else:
        return redirect(url_for("login")) 

@app.route("/add_water", methods=["POST", "GET"])
def add_water():
    if 'username' in session:
        water_new_value = request.form.get('water_num', None)
        new_date_value = session["day_today"]
        new_time_value = datetime.now().strftime('%H:%M')
        water_list = get_user_water(session['username'])
        water_list.append({"quantity": int(water_new_value), "time":new_time_value, "date": new_date_value})
        update_user(session["username"], "water", water_list)
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
                workout_list = get_user_workout(session['username'])
                if 0 <= workout_id <= len(workout_list):
                    workout_to_cahnge = workout_list[workout_id]
                    workout_to_cahnge["type"] = new_workout
                    workout_to_cahnge["duration"] = new_time_workout
                    update_user(session["username"], "workout", workout_list)
                    return redirect(url_for("profile"))
                else:
                    raise IndexError("Invalid workout_id")  
        elif action == "Reset":
            if 0 <= workout_id < len(workout_list):
                workout_list.pop(workout_id)
                update_user(session["username"], "workout", workout_list)

            else:
                raise IndexError("Invalid workout_id") 
            return redirect(url_for("profile"))
    else: 
        return redirect(url_for("login")) 
    
# For the weekly display, calculate the previous week and the next week, starting from 
# Monday. The display of today’s date is managed on the frontend.

def get_week_dates(start_date):
    start_date = datetime.strptime(start_date, '%d/ %m/ %Y')
    monday = start_date - timedelta(days=start_date.weekday())
    week_days = []
    for i in range(7):
        current_day = monday + timedelta(days=i)
        day_name = current_day.strftime('%A')
        day_to_append = {"day_name": day_name, 'day_date': current_day.strftime('%d/ %m/ %Y')}
        month_name = current_day.strftime('%B')
        week_days.append(day_to_append)
    return week_days, month_name



@app.route("/display_week")
def display_week():
    if 'username' in session:
        username = session["username"]
        profile = session['profile']
        color = session['color']
     
        meals = get_user_meals(username)
        workout = get_user_workout(username)
        water = get_user_water(username)
        weight = get_user_weight(username)
        fav_meal = get_user_fav_meals(username)
        if 'day_today' not in session:
            session['day_today'] = datetime.today().strftime('%d/ %m/ %Y')

        date_today = session['day_today']
        # print(date_today)
        week_days, month = get_week_dates(date_today)
        if profile.isalpha():
            profile = profile.upper()
        return render_template("week_display.html", username = username, 
                               profile = profile, 
                               color = color, 
                               fav_meals = fav_meal,
                               date = date_today,
                               week_days = week_days,
                               weight =weight,
                               water =  water,
                               workout = workout,
                               meals = meals,
                               month = month
                               )
    else: 
        return redirect(url_for("login"))
    

@app.route("/next_week", methods=["POST"])
def next_week():
    if 'username' in session:
        if 'day_today' not in session:
            session['day_today'] = datetime.today().strftime('%d/ %m/ %Y')
        date_today = session['day_today']
        start_day = datetime.strptime(date_today, '%d/ %m/ %Y')
        next_week_start_date = start_day + timedelta(weeks=1)
        session['day_today'] = next_week_start_date.strftime('%d/ %m/ %Y')
        return redirect(url_for("display_week"))
    else: 
        return redirect(url_for("login"))

@app.route("/prev_week", methods=["POST"])
def prev_week():
    if 'username' in session:
        if 'day_today' not in session:
            session['day_today'] = datetime.today().strftime('%d/ %m/ %Y')
        date_today = session['day_today']
        start_day = datetime.strptime(date_today, '%d/ %m/ %Y')
        prev_week_start_date = start_day - timedelta(weeks=1)
        session['day_today'] = prev_week_start_date.strftime('%d/ %m/ %Y')
        return redirect(url_for("display_week"))
    else: 
        return redirect(url_for("login"))

# When you press on a date, you can go to the page for that date and edit the data.

@app.route("/go_to_date/<path:date_now>", methods=["POST", "GET"])
def go_to_date(date_now):
    if 'username' in session:
        if request.method == 'POST':
         
            date_from = datetime.strptime(date_now, '%d/ %m/ %Y')
            session['day_today'] = date_from.strftime('%d/ %m/ %Y')
        return redirect(url_for("profile"))
    else:
         return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop('profile', None)
    session.pop("color", None)
    session.pop("day_today", None)

    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = False, port = 8080)

main = app