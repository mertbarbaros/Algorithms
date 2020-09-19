#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:06:51 2020

@author: mertbarbaros
"""


import urllib.request, urllib.parse, urllib.error
import json


#We will add the location to the end of this address
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    #input expecting location like Ann Arbor, HI
    address =input('Enter Location:  ')
    #if the location is empty break
    if len(address) < 1: break
    #parse the location the the end of the serviceurl
    url = serviceurl + urllib.parse.urlencode({'address': address})
    
    print('Retrieving', url)
    """
    Result should be like
    Retrieving 
    https://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
    """
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'charachters')
    
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    #if js is empty or status key is not in js dict
    #or status value is not OK, then we have a problem
    if not js or 'status' not in js or js['status'] !=  'OK':
        print('==== Failure to Retrieve ====')
        print(data)
        continue
    
    # [0] for first result
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['resulsts'][0]['formatted_address']
    print(location)
    
    
