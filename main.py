from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import secrets
import logging 

secret_key = secrets.token_hex(16)



users =[{
    "name": "roni", 
    "password": "1234", 
    "color": "#206A5D"
    }]

colors = ["#206A5D", "#81B214", "#FFCC29", "#F58634"]

weight_input = []
meals_list = []
water_list = []
workout_list =[]
favorite_meals = [{"Breakfast": "2 slices of bread"},
                   {"Lunch": "Salat"},
                   {"Dinner": "Chicken with rice and vegtables"},
                   {"Supper": "tomato soap"}]


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
    else: return  

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
        # print(color)
        if password == password2 and color:
            new_user = {"name": name, "password": password, "color": color}
            session['username'] = name
            session['profile'] = name[0]
            session["color"] = color
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
        if profile.isalpha():
            profile = profile.upper()
        return render_template("home.html", username = username, profile = profile, color = color, meals = favorite_meals)
    else: 
        return redirect(url_for("login"))

  
@app.route("/weight", methods = ["POST"])
def weight():
    if request.method == 'POST':
        data = request.get_json()
        weight_unit = data.get('weight')
        measurement = data.get('measurement')
        response_data = {
            "weight_unit" : measurement,
            "weight_num": weight_unit
        }
        weight_input.append(response_data)
        # session['weight'] = weight_input
        # print(session)
        return jsonify(response_data)

@app.route("/meals", methods = ["POST"])
def meals():
        data = request.get_json()
        meal = data.get('meal')
        time = data.get('time')
        date = data.get('date')
        response_data = {
            "meal" : meal,
            "time": time,
            "date" : date
        }
        favorite_meals.append(response_data)
        print(favorite_meals)
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
            if profile.isalpha():
                profile = profile.upper()
                return  render_template("add_meal.html", username = username, profile = profile, color = color, meals = favorite_meals)
        else: 
            return redirect(url_for("login"))
        
@app.route("/meal_edited", methods=["POST"])
def meal_edited():
    try:
         data =request.get_json()
         print(data)
         if not isinstance(data, list):
              raise ValueError("Expecting a list of meals")
         favorite_meals =[]
         for item in data:
              name = item.get('name')
              content = item.get("content")
              favorite_meals.append({"name": name, "content": content})
         logging.debug(f"Received Meals List: {favorite_meals}")
         return jsonify(favorite_meals)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug = True, port = 8080)