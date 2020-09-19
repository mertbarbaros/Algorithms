#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:44:40 2020

@author: mertbarbaros
"""


import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl 
import hidden


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print(' ')
    acct = input('Enter Twitter Username: ')
    
    if( len(acct) < 1) : break
    
    url = twurl.augement(TWITTER_URL,
                         {'screen_name': acct, 'count': '5'})
    
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent =4))
    
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ', s[:50])
