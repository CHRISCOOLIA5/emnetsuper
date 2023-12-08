#!/usr/bin/env python
import time
import socket
import colorama
from colorama import Fore
text = """
███████╗███╗   ███╗███╗   ██╗███████╗████████╗   N 
██╔════╝████╗ ████║████╗  ██║██╔════╝╚══██╔══╝   E 
█████╗  ██╔████╔██║██╔██╗ ██║█████╗     ██║      T 
██╔══╝  ██║╚██╔╝██║██║╚██╗██║██╔══╝     ██║      W 
███████╗██║ ╚═╝ ██║██║ ╚████║███████╗   ██║      O 
╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝      R
Pre-Beta v1.2                    In Development  K
"""
yoo = """
╔═══════════════════════════════════════════════════╗
║Login/Signup     By Chris     Type Help for Support║
╠═══════════════════════════════════════════════════╣ 
║              All Right Reserved 2023©             ║
╚═══════════════════════════════════════════════════╝                                               
"""
print(Fore.RED, text)
print(Fore.MAGENTA, yoo)
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
print('[+]  Going Online')
s.connect((TCP_IP, TCP_PORT))
print('[+]  Connected')
s.send(MESSAGE)
time.sleep(2)
s.send(MESSAGE2)
data = s.recv(BUFFER_SIZE)
dataw = s.recv(BUFFER_SIZE)
s.close()
dataln = data.decode()
datalma = dataw.decode()
print('[+] Sent:', dataln, datalma)