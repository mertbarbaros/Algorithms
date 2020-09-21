# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:50:49 2020

@author: barbarosblog
"""

import urllib.request
import urllib.parse
import urllib.error
import ssl
import json

#default api key
api_key= False

#api key and target service url
if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#JSON 

while True:
    address = 'Western Governors University'
    if len(address) < 1 : break
    
    parms = dict()
    parms['address'] = address
    
    if api_key is not False: parms['key'] = api_key
    url = service_url + urllib.parse.urlencode(parms)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'charachters')
    
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=====Failure to Retirive======')
        print(data)
        continue
    
    print(json.dumps(js, indent = 4))
    
    place_id = js['results'][0]['place_id']
    print('Place id is', place_id)
