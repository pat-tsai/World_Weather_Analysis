#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from citipy import citipy
from config import weather_api_key
import numpy as np


# In[2]:


lat = np.random.uniform(-90.000, 90.000, size=2000)
lng = np.random.uniform(-180.000, 180.000, size=2000)
lnglat = zip(lat,lng)


# In[3]:


coordinates = list(lnglat)


# In[4]:


coordinates


# In[5]:


city_list = []
country_list = []

# finding nearest city to coordinates
for coordinate in coordinates:
    city = citipy.nearest_city(coordinate[0],coordinate[1]).city_name
    country = citipy.nearest_city(coordinate[0],coordinate[1]).country_code.upper()
    
    if city not in city_list:   
        city_list.append(city)
        country_list.append(country)


# In[6]:


city_list


# In[7]:


url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key
set_count = 0
item_count = 0
    
weather_data = []

for index, city in enumerate(city_list):
    print(city, index)
    if(index % 100 == 0 and index>=100):
        set_count += 1
        item_count = 1
        
        # Create endpoint URL with each city, remove black spaces in url to search for exact city names
    city_url = url + "&q=" + city.replace(" ","+")
    print(city_url)
        
    try:
        city_weather = requests.get(city_url).json()
        
        city_lat = city_weather['coord']['lat']
        city_lng = city_weather['coord']['lon']
        city_temp = city_weather['main']['temp_max']
        city_humidity = city_weather['main']['humidity']
        city_clouds = city_weather['clouds']['all']
        wind_speed = city_weather['wind']['speed']
        city_descr = city_weather['weather'][0]['description']

        columns = {'City':city,
                   'Country':country_list[index],
                   'Lat':city_lat,
                   'Lng':city_lng,
                   'Max Temp':city_temp,
                   'Humidity':city_humidity,
                   'Cloudiness':city_clouds,
                   'Wind Speed':wind_speed,
                   'Current Description':city_descr
        }

        weather_data.append(columns)
    except (KeyError):
        print("City info N/A... skipping")
        pass
    


# In[8]:


weather_data_df = pd.DataFrame(weather_data)
weather_data_df.head()


# In[9]:


# Create the output file (CSV).
output_data_file = "WeatherPy_Database.csv"
# Export the City_Data into a CSV.
weather_data_df.to_csv(output_data_file, index_label="City_ID")


# In[ ]:




