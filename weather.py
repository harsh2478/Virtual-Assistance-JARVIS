#Code to mark location on map :
    #from geopy.geocoders import Nominatim
    #import folium

    #geolocator = Nominatim(user_agent="geoExercises")
    #location = geolocator.geocode("Ashok vihar, delhi")
    #print("The latitude of the location is: ", location.latitude)
    #print("The longitude of the location is: ", location.longitude)

    #map = folium.Map(location=[28.6885171, 77.1739339], zoom_start=13)
    #point = [28.6885171, 77.1739339]
    #mylocation = folium.Marker(point, popup='My Home', icon=folium.Icon()).add_to(map)

import requests

def weather_api():
    api_key = "639f2a1fca3adbf636c6811607045db8"
    weather_api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={28.6885171}&lon={77.1739339}&appid={api_key}"
    response = requests.get(weather_api_url)
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    feels_like = weather_data['main']['feels_like']
    speed = weather_data['wind']['speed']
    weather_description = weather_data['weather'][0]['description']

    celsius = lambda x: x - 273.15 # This is because the unit of temperature is by default in kelvin
    print("Weather : ", weather_description)
    print("Temperature :",celsius(temperature),"°C")
    print("Feels like :", celsius(feels_like), "°C")
    print("Humidity :", humidity,"%")
    print("Wind", speed, "m/sec")





