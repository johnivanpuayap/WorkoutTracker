import os
import requests
from config import *
from datetime import datetime

# Data
TODAY = datetime.now()
DATE = TODAY.strftime("%d/%m/%Y")
TIME = TODAY.strftime("%X")

# API stuff
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
NUTRITIONIX_HEADERS = {
    "x-app-id": os.environ['NUTRITIONIX_API_ID'],
    "x-app-key": os.environ['NUTRITIONIX_API_KEY'],
}
SHEETY_ENDPOINT = 'https://api.sheety.co/c4ee1ee692651edb4c7ee96edf35311b/myWorkouts/workouts'
SHEETY_HEADERS = {
    "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
}

user_query = input("Tell me what exercise you did: ")

nutritionix_parameters = {
    "query": user_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_parameters, headers=NUTRITIONIX_HEADERS)
exercise_data = nutritionix_response.json()['exercises']

for exercise in exercise_data:
    # Add data to rows
    sheety_parameters = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    print(sheety_parameters)

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=SHEETY_HEADERS)
    sheety_response.raise_for_status()
    if sheety_response.status_code == 200:
        print('Added new row')