#!/usr/bin/env python
# coding: utf-8

# ## Deliverable 3. Create a Travel Itinerary Map.

# In[238]:


# Dependencies and Setup
import pandas as pd
import requests
import gmaps

# Import API key
from config import g_key

# Configure gmaps
gmaps.configure(api_key=g_key)


# In[239]:


# 1. Read the WeatherPy_vacation.csv into a DataFrame.
vacation_df = pd.read_csv("../Vacation_Search/hotel_list.csv")
vacation_df.head()


# In[240]:


# 2. Using the template add the city name, the country code, the weather description and maximum temperature for the city.
info_box_template = """
<dl><dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
<dt>Max Temp</dt><dd>{Max Temp} °F</dd>
<dt>Description:</dt><dd>{Current Description}</dd>
</dl>
"""
clean_hotel_df = vacation_df.dropna()
# 3a. Get the data from each row and add it to the formatting template and store the data in a list.
vacation_list = [info_box_template.format(**row) for index, row in clean_hotel_df.iterrows()]

# 3b. Get the latitude and longitude from each row and store in a new DataFrame.
locations = clean_hotel_df[["Lat", "Lng"]]
locations_df = pd.DataFrame(locations)


# In[241]:


# 4a. Add a marker layer for each city to the map.

fig = gmaps.figure(center=(18.0, 15.0), zoom_level=2.3)

marker_layer = gmaps.marker_layer(locations_df, info_box_content=info_box_template)

fig.add_layer(marker_layer)

# 4b. Display the figure
fig


# In[ ]:





# In[254]:


# From the map above pick 4 cities and create a vacation itinerary route to travel between the four cities. 
# 5. Create DataFrames for each city by filtering the 'vacation_df' using the loc method. 
# Hint: The starting and ending city should be the same city.

import random

# finding which countries have the most cities from our randomly selected subset
vacation_df.groupby('Country').count().reset_index().sort_values(('City_ID'), ascending=False)

country_filtered_df = vacation_df.loc[(vacation_df['Country']=='BR')]
vacation_start = filtered_df.iloc[[0]]


#temp = vacation_start['Max Temp']
#max_temp = temp + 9
#min_temp = temp - 9

vacation_end = vacation_start

temp_filtered_df = country_filtered_df[(country_filtered_df['Max Temp'] <= max_temp) & 
                                       (country_filtered_df['Max Temp'] >= min_temp) &
                                       (country_filtered_df['City'] != filtered_df.iloc[0]['City'])]

indices = random.sample(range(0,len(temp_filtered_df)),3)

vacation_stop1 = temp_filtered_df.iloc[[indices[0]]]
vacation_stop2 = temp_filtered_df.iloc[[indices[1]]]
vacation_stop3 = temp_filtered_df.iloc[[indices[2]]]
temp_filtered_df


# In[ ]:





# In[266]:


# 6. Get the latitude-longitude pairs as tuples from each city DataFrame using the to_numpy function and list indexing.
import numpy as np

specific_country = temp_filtered_df[['Lat','Lng']]
coordinates = specific_country.to_numpy()
start = tuple(coordinates[1])
end = tuple(coordinates[1])
stop1 = tuple(coordinates[2])
stop2 = tuple(coordinates[3])
stop3 = tuple(coordinates[4])
start, stop1, stop2, stop3, end


# In[287]:


# 7. Create a direction layer map using the start and end latitude-longitude pairs,
# and stop1, stop2, and stop3 as the waypoints. The travel_mode should be "DRIVING", "BICYCLING", or "WALKING".
import gmaps
import gmaps.datasets
from config import g_key
gmaps.configure(api_key = g_key)


base_url = 'http://maps.googleapis.com/maps/api/directions/json?'

fig = gmaps.figure()
wholeTrip = gmaps.directions_layer(start, end, waypoints=[stop3, stop2, stop1], show_markers=True, travel_mode='DRIVING', stroke_weight=3.0, stroke_opacity=1.0)
fig.add_layer(wholeTrip)

fig


# In[276]:


# 8. To create a marker layer map between the four cities.
#  Combine the four city DataFrames into one DataFrame using the concat() function.
itinerary_df = pd.concat([vacation_start, vacation_stop1, vacation_stop2, vacation_stop3, vacation_end],keys=('vacation_start', 'vacation_stop1', 'vacation_stop2', 'vacation_stop3', 'vacation_end'),ignore_index=True)
itinerary_df


# In[277]:


# 9 Using the template add city name, the country code, the weather description and maximum temperature for the city. 
info_box_template = """
<dl>
<dt>Hotel Name</dt><dd>{Hotel Name}</dd>
<dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
<dt>Max Temp</dt><dd>{Max Temp} °F</dd>
<dt>Description:</dt><dd>{Current Description}</dd>
</dl>
"""

# 10a Get the data from each row and add it to the formatting template and store the data in a list.
city_info = [info_box_template.format(**row) for index, row in itinerary_df.iterrows()]

# 10b. Get the latitude and longitude from each row and store in a new DataFrame.
locations = pd.DataFrame({'Lat': (start[0],stop1[0],stop2[0],stop3[0],end[0]),
                          'Lng': (start[1],stop1[1],stop2[1],stop3[1],end[1])})
locations


# In[286]:


# 11a. Add a marker layer for each city to the map. 

fig = gmaps.figure(center=(-10.60, -43.46), zoom_level=4)

marker_layer = gmaps.marker_layer(locations, info_box_content=city_info)

fig.add_layer(marker_layer)

# 11b. Display the figure
fig


# In[ ]:




