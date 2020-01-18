# -*- coding: utf8 -*-
import json

import googlemaps
google_key = "AIzaSyDW-GIfy8FarJJyH5D_4YRicBPYEcjLnr0"
gmaps = googlemaps.Client(key = google_key)

place = "USC"

geocode_result = gmaps.geocode("Los Angeles")
loc = geocode_result[0]["geometry"]["location"]
place_results = gmaps.places_nearby(location = loc, radius = 10000, keyword = place)

#print(json.dumps(place_results))
dest_id = place_results['results'][0]['place_id']
#print(dest_id)

dest_addr = ""
dest_info = gmaps.place(dest_id, language = "zh-tw")
#print(json.dumps(dest_info))



print(str(dest_info['result']['formatted_address']))

