import os
import requests
from config import *
from datetime import datetime

# Data
TODAY = datetime.now()
DATE = TODAY.strftime("%d/%m/%Y")
TIME = TODAY.strftime("%H:%M")

# API stuff
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    "x-app-id": os.environ['NUTRITIONIX_API_ID'],
    "x-app-key": os.environ['NUTRITIONIX_API_KEY'],
}

GOOGLE_SHEETS_LINK = 'https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit#gid=0'

exercise_data = input("Tell me what exercise you did: ")

exercise_parameters = {
    "query": exercise_data,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_parameters, headers=headers)
exercise_data = response.json()['exercise']