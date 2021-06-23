# SHAPEAI PYTHON AND CYBER SECURITY BOOTCAMP
# NAME:-SHASHWAT SHETH
# EMAIL:-SHETHSHASHWAT26@GMAIL.COM

# WEATHER FORECAST THROUGH API USING PYTHON PROJECT

import requests
from datetime import datetime

api_key = '50f84a5ac3ef32f07f5c1c14d3d7cf70'
location = str(input("Enter the city name: "))

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
cont = api_data.copy()  

with open('data.txt','w') as file:
    file.write(str(cont))
    file.close()

if api_data['cod']=='404':
    print(api_data['message'])
else:
    coord_long = api_data['coord']['lon']
    coord_lat = api_data['coord']['lat']
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    pressure = api_data['main']['pressure']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    sys_country = api_data['sys']['country']
    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")
    print ("Current temperature is: {:.2f} degree Celsius".format(temp_city))
    print("Country               :",sys_country)
    print("latittude Cordinates  :",coord_lat)
    print("Longitude Cordinates  :",coord_long)
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",hmdt, '%')
    print("Current Pressure      :",pressure,"atm")
    print ("Current wind speed    :",wind_spd ,'kmph')
    print ("-------------------------------------------------------------")
    
# THANKYOU