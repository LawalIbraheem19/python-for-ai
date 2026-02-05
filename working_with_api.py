import requests

# We need coordinates to get weather data
latitude = -20.425142499999996   # Ilha Solteira latitude
longitude = -51.33708733068913   # Ilha Solteira longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data.keys())

temperature = data["current"]["temperature_2m"]
time = data["current"]["time"]
print(f"The current temperature recorded in Ilha Solteira is {temperature} and the time is {time}")

# Write a function to get the weather details of a locality
def get_weather(latitude, longitude):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()

    return data["current"]["temperature_2m"], data["current"]["time"], data["elevation"]


Ilha_temp, Ilha_time, Ilha_elev = get_weather(latitude = -20.425142499999996, longitude = -51.33708733068913 )

print(f"Ilha Solteira temperature: {Ilha_temp}°C")
print(f"Ilha Solteira time: {Ilha_time}")
print(f"Ilha Solteira elevation: {Ilha_elev}m")