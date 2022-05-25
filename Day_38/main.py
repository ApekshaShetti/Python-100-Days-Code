import requests

GENDER = "FEMALE"
WEIGHT_KG = "42"
HEIGHT_CM = "154"
AGE = "21"

APP_ID = "1a4849ef"
API_KEY = "027d4fd764b13cac3cc9bbf09d3de973"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)