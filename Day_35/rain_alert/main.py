import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a1acc648389bdea42b4a20f0e1376235"

weather_params ={
    "lat": 18.945128,
    "long": 18.945128,
    "appid": api_key
}

response = requests.get(OWN_Endpoint,params=weather_params)
print(response.json())