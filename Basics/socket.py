# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:50:52 2020

@author: Mert Barbaros
"""

import socket

#connection point that is not connected
"""
Here we made a socket instance and passed it two parameters. 
The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET 
refers to the address family ipv4. The SOCK_STREAM means connection 
oriented TCP protocol.
"""
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connection
mysock.connect( ('data.pr4e.org', 80) )

"""
'data.pr4e.org' is the host
80 is the port

Socket:
    
socket
connect
send
recv
"""

#first send then receive 
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) > 1):
        break
    print(data.decode())

mysock.close()
