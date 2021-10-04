import json
import requests

user_input = input("Enter your ip: ")

r = requests.get(f"https://ipapi.co/{user_input}/json/")

data = json.loads(r.text)

with open('data.json', 'w') as f:
    json.dump(data, f)

print("IP: ", data['ip'])
print("Version: ", data['version'])
print("City: ", data['city'])
print("Region: ", data['region'])
print("Country Name: ", data['country_name'])
print("Latitude: ", data['latitude'])
print("Longitude: ", data['longitude'])
print("TimeZone: ", data['timezone'])
print("Country Population: ", data['country_population'])
print("Organization: ", data['org'])
