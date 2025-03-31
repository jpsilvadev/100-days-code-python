import requests
from datetime import datetime

APP_ID = "SOME ID"
API_KEY = "SOME KEY"

exercises = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

nutritionix_params = {
    "query": exercises,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 175.00,
    "age": 24,
}


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(
    url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers
)

output = response.json()


current_time = datetime.now()

date = current_time.strftime("%d/%m/%Y")
time = current_time.strftime("%H:%M:%S")
exerc = output["exercises"][0]["name"].title()
duration = output["exercises"][0]["duration_min"]
cals = output["exercises"][0]["nf_calories"]

output_to_sheet = {
    "workout": {
        "Date": date,
        "Time": time,
        "Exercise": exerc,
        "Duration": duration,
        "Calories": cals,
    }
}


sheety_post_endpoint = (
    "https://api.sheety.co/4ff602b6f555b0c3dd19c4eb6e30f9a0/workoutTracker/workouts"
)

print(output_to_sheet)
sheety_response = requests.post(url=sheety_post_endpoint, json=output_to_sheet)
print(sheety_response.json())
