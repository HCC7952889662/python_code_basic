# -*- coding: utf8 -*-
import json

import random

place = "USC"
addr = ""
out = ""
kw = "food"

import googlemaps
google_key = "AIzaSyDW-GIfy8FarJJyH5D_4YRicBPYEcjLnr0"
gmaps = googlemaps.Client(key = google_key)



geocode_result = gmaps.geocode(place)
loc = geocode_result[0]["geometry"]["location"]
radar_results = gmaps.places_nearby(location = loc, radius = 400, keyword = kw)
#print (json.dumps(radar_results))

radar_results = radar_results['results']
radar_result = random.choice( radar_results )
#    place_name = radar_result['name']
place_id = radar_result['place_id']
#    print (place_id)
#find daily information about the place
detail_info = gmaps.place(place_id, language = "en-US")
#        print (json.dumps(detail_info))
f= open("Choose.txt","w+")
for i in detail_info['result']:
    if(i == 'opening_hours'):
        place_name = detail_info['result']['name']
        print(place_name)
        f.write(place_name+"\n")
        for j in range(0,len(detail_info['result']['address_components'])):
            addr = detail_info['result']['address_components'][j]['long_name'] + addr
        print(str(addr))
        f.write(str(addr)+"\n")
        addr = ""
        for day in range(0,6):
            weekday_text = detail_info['result']['opening_hours']['weekday_text'][day]
            print (weekday_text)
            f.write(weekday_text+"\n")
        break

f.close()
from google_speech import Speech

# say "Hello World"
lang = "en"
speech = Speech(place_name, lang)
speech.play()
#for python3

#    rating = radar_result['rating']
#    print (place_name.encode('utf-8') + "  rating : " + str(rating))
