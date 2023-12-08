#!/usr/bin/env python
import time
import socket
text = """
███████╗███╗   ███╗███╗   ██╗███████╗████████╗    
██╔════╝████╗ ████║████╗  ██║██╔════╝╚══██╔══╝    
█████╗  ██╔████╔██║██╔██╗ ██║█████╗     ██║       
██╔══╝  ██║╚██╔╝██║██║╚██╗██║██╔══╝     ██║       
███████╗██║ ╚═╝ ██║██║ ╚████║███████╗   ██║       
╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝       
                                                  
"""
print(text)
login = input("Username:")
passw = input("Password:")
 
TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 1024
my_str = (login)
my_str2 = (passw)
MESSAGE = str.encode(my_str)
MESSAGE2 = str.encode(my_str2)
print('[+]  Connecting')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('[!]  Going Online')
s.connect((TCP_IP, TCP_PORT))
print('[+] Connected')
s.send(MESSAGE)
time.sleep(2)
s.send(MESSAGE2)
data = s.recv(BUFFER_SIZE)
dataw = s.recv(BUFFER_SIZE)
s.close()
dataln = data.decode()
datalma = dataw.decode()
print('[+] Sent:', dataln, datalma)