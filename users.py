users =[{
    "name": "roni", 
    "password": "1234", 
    "color": "#206A5D",
    "water": [],
    "weight": [],
    "meals": [],
    "workout": [],
    "fav_meals" : [{"Breakfast": "2 slices of bread"},
                   {"Breakfast": "2 slices of bread"},
                   {"Lunch": "Salat"},
                   {"Dinner": "Meat with rice and vegtables"},
                   {"Supper": "tomato soap"}]
    },{
    "name": "w", 
    "password": "1", 
    "color": "#206A5D",
    "water": [],
    "weight": [],
    "meals": [],
    "workout": [],
    "fav_meals" : [{"Breakfast": "2 slices of bread"},
                   {"Lunch": "Salat"},
                   {"Dinner": "Chicken with rice and vegtables"},
                   {"Supper": "tomato soap"}]
    }
    ]

class User:
    def __init__(self, name, password, color):
        self.username = name
        self.password = password
        self.color = color
        self.water = []
        self.weight = []
        self.meals= []
        self.workout = []
        self.fav_meals = []
    
    def add_water(self, object):
        if object:
            self.water.append(object)
        return self.water

    def add_weight(self, object):
        if object:
            self.weight.append(object)
        return self.weight
    
    def add_meals(self, object):
        if object:
            self.meals.append(object)
        return self.meals
    
    def add_workout(self, object):
        if object:
            self.workout.append(object)
        return self.workout

    def get_fav_meals(self):
        return self.fav_meals
    
    def load_fav_meals(self, list):
        if list:
            self.fav_meals = list

    def __str__(self):
        return (f'{{\n'
                f'    "name": "{self.username}",\n'
                f'    "password": "{self.password}",\n'
                f'    "color": "{self.color}",\n'
                f'    "water": {self.water},\n'
                f'    "weight": {self.weight},\n'
                f'    "meals": {self.meals},\n'
                f'    "workout": {self.workout},\n'
                f'    "fav_meals": {self.fav_meals}\n'
                f'}}')